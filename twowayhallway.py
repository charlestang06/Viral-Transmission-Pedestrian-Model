import random as rnd
from tkinter import *
import time
from math import sin, cos, sqrt, exp
import numpy as np


open('processing/sim_output.txt', 'w').close()
vars = open('processing/variables.txt', 'r')
contents = vars.readlines()
contents[0] = list(map(float, contents[0].split()))

# Environmental Specifications
num = int(contents[0][0])   # number of agents
s = contents[0][1]  # environment size in meters
velocity = contents[0][2]
hallway = int(contents[0][3]) #0 = false, 1 = true
total_checks = 0
total_interactions = 0
check_every = 0.1 #sec

# Agent Parameters (play with these)
k = 1.5
m = 2.0
t0 = 3
rad = .2  # Collision radius
sight = float(contents[0][10])
maxF = 5  # Maximum force/acceleration

frac_of_circ = int(contents[0][5])
community_range = int(contents[0][6])
num_community = int(contents[0][7])

angs_arr = []
for x in range(frac_of_circ*2):
    angs_arr.append(np.pi * x / frac_of_circ)

pixelsize = 1000
framedelay = 5
drawVels = True

win = Tk()
win.iconify()
canvas = Canvas(win, width=pixelsize, height=pixelsize, background="#444")
canvas.pack()

# Initialized variables
ittr = 0
c = []  # center of agent
v = []  # velocity
gv = []  # goal velocity
nbr = []  # neighbor list
nd = []  # neighbor distance list
QUIT = False
paused = False
step = False

circles = []
velLines = []
gvLines = []
text = []
barrier = []

def initSim():
    global rad

    print("")

    for i in range(num_community): #initiates cluster agents
        circles.append(canvas.create_oval(0, 0, rad, rad, fill="white", tags = num))
        text.append(canvas.create_text(0, 0,fill="black",font="Times 15 italic bold",text=str(i+1)))
        velLines.append(canvas.create_line(0, 0, 10, 10, fill="red"))
        gvLines.append(canvas.create_line(0, 0, 10, 10, fill="green"))

        c.append(np.zeros(2))
        v.append(np.zeros(2))
        gv.append(np.zeros(2))
        c[i][0] = rnd.uniform(s-2*community_range, s-community_range) #sets the coordinates within these bounds
        c[i][1] = rnd.uniform(community_range, 2*community_range)
        gv[i] = 1.5 * np.copy(v[i])
        canvas.itemconfig(circles[i], fill="magenta") #colors community agents red

    for i in range(num_community, num):
        circles.append(canvas.create_oval(0, 0, rad, rad, fill="white", tags = num))
        text.append(canvas.create_text(0, 0,fill="black",font="Times 15 italic bold",text=str(i+1)))
        velLines.append(canvas.create_line(0, 0, 10, 10, fill="red"))
        gvLines.append(canvas.create_line(0, 0, 10, 10, fill="green"))
        c.append(np.zeros(2))
        v.append(np.zeros(2))
        gv.append(np.zeros(2))
        c[i][0] = rnd.uniform(0, s)
        c[i][1] = rnd.uniform(0, s)
        if c[i][1]>=s/2 - rnd.randrange(int(-s*3/5), int(s*3/5)):
            ang = rnd.uniform(np.pi-0.2,np.pi+0.2)
        else:
            ang = rnd.uniform(-0.2, 0.2)
        v[i][0] = cos(ang)*velocity
        v[i][1] = sin(ang)*velocity
        gv[i] = 1.5 * np.copy(v[i])


def drawWorld():
    global rad, s
    for i in range(num):
        scale = pixelsize / s
        canvas.coords(circles[i], scale * (c[i][0] - rad), scale * (c[i][1] - rad), scale * (c[i][0] + rad),
                      scale * (c[i][1] + rad))
        canvas.coords(velLines[i], scale * c[i][0], scale * c[i][1], scale * (c[i][0] + 1. * rad * v[i][0]),
                      scale * (c[i][1] + 1. * rad * v[i][1]))
        if i > num_community:
            canvas.coords(gvLines[i], scale * c[i][0], scale * c[i][1], scale * (c[i][0] + 1. * rad * gv[i][0]),
                          scale * (c[i][1] + 1. * rad * gv[i][1]))
        canvas.coords(text[i], scale * c[i][0], scale * c[i][1])

        if drawVels:
            canvas.itemconfigure(velLines[i], state="normal")
            canvas.itemconfigure(gvLines[i], state="normal")
        else:
            canvas.itemconfigure(velLines[i], state="hidden")
            canvas.itemconfigure(gvLines[i], state="hidden")
        double = False
        newX = c[i][0]
        newY = c[i][1]
        if c[i][0] < rad:
            newX += s
            double = True
        if c[i][0] > s - rad:
            newX -= s
            double = True
        if c[i][1] < rad:
            newY += s
            double = True
        if c[i][1] > s - rad:
            newY -= s
            double = True
        if double:
            pass

def findNeighbors():
    global nbr, nd, c, contacts_close, contacts_far, total_interactions
    contacts_close = []
    contacts_far = []
    nbr = []
    nd = []
    for i in range(num):
        nbr.append([])
        nd.append([])
        for j in range(num):
            if i == j: continue
            d = c[i] - c[j]
            if d[0] > s / 2.: d[0] = s - d[0]
            if d[1] > s / 2.: d[1] = s - d[1]
            if d[0] < -s / 2.: d[0] = d[0] + s
            if d[1] < -s / 2.: d[1] = d[1] + s
            l2 = d.dot(d)
            s2 = sight**2
            if l2 < s2:
                nbr[i].append(j)
                nd[i].append(sqrt(l2))
                if [j, i] not in contacts_close:
                    contacts_close.append([i, j])
                    total_interactions += 1



def E(t):
    return (B / t ** m) * exp(-t / t0)


def rdiff(pa, pb, va, vb, ra, rb):
    p = pb - pa  # relative position
    return (sqrt(p.dot(p)))


def ttc(pa, pb, va, vb, ra, rb):
    maxt = 999

    p = pb - pa  # relative position
    if p[0] > s / 2.: p[0] = p[0] - s
    if p[1] > s / 2.: p[1] = p[1] - s
    if p[0] < -s / 2.: p[0] = p[0] + s
    if p[1] < -s / 2.: p[1] = p[1] + s
    rv = vb - va  # relative velocity

    a = rv.dot(rv)
    b = 2 * rv.dot(p)
    c = p.dot(p) - (ra + rb) ** 2

    det = b * b - 4 * a * c
    t1 = maxt
    t2 = maxt
    if (det > 0):
        t1 = (-b + sqrt(det)) / (2 * a)
        t2 = (-b - sqrt(det)) / (2 * a)
    t = min(t1, t2)

    if (t < 0 and max(t1, t2) > 0):  # we are colliding
        t = 100  # maybe should be 0?
    if (t < 0): t = maxt
    if (t > maxt): t = maxt


    return t


def dE(pa, pb, va, vb, ra, rb):
    global k, m, t0
    INFTY = 999
    maxt = 999

    w = pb - pa
    if w[0] > s / 2.: w[0] = w[0] - s  # wrap around for torus
    if w[1] > s / 2.: w[1] = w[1] - s
    if w[0] < -s / 2.: w[0] = w[0] + s
    if w[1] < -s / 2.: w[1] = w[1] + s
    v = va - vb
    radius = ra + rb
    dist = sqrt(w[0] ** 2 + w[1] ** 2)
    if radius > dist: radius = .99 * dist
    a = v.dot(v)
    b = w.dot(v)
    c = w.dot(w) - radius * radius
    discr = b * b - a * c
    if (discr < 0) or (a < 0.001 and a > - 0.001): return np.array([0, 0])
    discr = sqrt(discr)
    t1 = (b - discr) / a

    t = t1

    if (t < 0): return np.array([0, 0])
    if (t > maxt): return np.array([0, 0])

    d = k * exp(-t / t0) * (v - (v * b - w * a) / (discr)) / (a * t ** m) * (m / t + 1 / t0)

    return d


def update(dt):
    global c
    findNeighbors()

    F = []  # force

    for i in range(num):
        F.append(np.zeros(2))

    for i in range(num):

        F[i] += (gv[i] - v[i]) / .5
        F[i] += 1 * np.array([rnd.uniform(-1., 1.), rnd.uniform(-1., 1.)])

        for n, j in enumerate(nbr[i]):  # j is neighboring agent

            t = ttc(c[i], c[j], v[i], v[j], rad, rad)

            d = c[i] - c[j]
            if d[0] > s / 2.: d[0] = d[0] - s  # wrap around for torus
            if d[1] > s / 2.: d[1] = d[1] - s
            if d[0] < -s / 2.: d[0] = s + d[0]
            if d[1] < -s / 2.: d[1] = s + d[1]

            r = rad
            dist = sqrt(d.dot(d))
            if dist < 2 * rad: r = dist / 2.001  # shrink overlapping agents

            dEdx = dE(c[i], c[j], v[i], v[j], r, r)
            FAvoid = -dEdx

            mag = np.sqrt(FAvoid.dot(FAvoid))
            if (mag > maxF): FAvoid = maxF * FAvoid / mag

            F[i] += FAvoid

    for i in range(num_community):
        a = F[i]
        v[i][0] = cos(angs_arr[i % (frac_of_circ * 2)]) * velocity  # goes in circles with small degree changes specified in frac_of_circle
        v[i][1] = sin(angs_arr[i % (frac_of_circ * 2)]) * velocity
        c[i] += v[i] * dt

        if c[i][0] < 0: c[i][0] = s
        if c[i][1] < 0: c[i][1] = s
        if c[i][0] > s: c[i][0] = 0
        if c[i][1] > s: c[i][1] = 0

    for i in range(num_community, num):  # velocity updates for the rest of the agents
        a = F[i]
        v[i] += a * dt
        c[i] += v[i] * dt
        if c[i][0] < 0: c[i][0] = s
        if c[i][1] < 0: c[i][1] = s
        if c[i][0] > s: c[i][0] = 0
        if c[i][1] > s: c[i][1] = 0

    temp = angs_arr[0]
    angs_arr.pop(0)
    angs_arr.append(temp)

def on_key_press(event):
    global paused, step, QUIT, drawVels
    if event.keysym == "space":
        paused = not paused
    if event.keysym == "s":
        step = True
        paused = False
    if event.keysym == "v":
        drawVels = not drawVels
    if event.keysym == "Escape":
        QUIT = True

flag = 0

def drawFrame(dt=.05):
    global start_time, step, paused, ittr, flag, total_checks
    if ittr > maxIttr or QUIT:  # Simulation Loop
        print("%s itterations ran ... quitting" % ittr)
        win.destroy()
    else:
        start_time = time.time()
        elapsed_time = time.time() - start_time
        if not paused:
            update(0.02)
            ittr += 1
        drawWorld()
        if step == True:
            step = False
            paused = True

        win.title("Normal Simulation - COVID Contact Tracing App")
        win.after(int(framedelay), drawFrame)
    if flag % 1 == 0:
        total_checks += 1
        with open('processing/sim_output.txt', 'a') as output:
            output.write(f'Check Num (every {check_every} seconds): {total_checks}\n')
            output.write(f'Close Contacts: {len(contacts_close)}\n')
            for pair in contacts_close:
                output.write(f'{pair[0]} {pair[1]}\n')
        if flag % 100 == 0:
            print(f'check: {flag}')
        if flag >= 600:
            print('60 Seconds Finished')
            exit()
    flag += 1

win.bind("<space>", on_key_press)
win.bind("s", on_key_press)
win.bind("<Escape>", on_key_press)
win.bind("v", on_key_press)

initSim()
maxIttr = 50000

win.after(framedelay, drawFrame)
mainloop()


