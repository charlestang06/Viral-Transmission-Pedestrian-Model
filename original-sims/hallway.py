import random as rnd
from tkinter import *
import time
from math import sin, cos, sqrt, exp
import numpy as np

open('../sim_output.txt', 'w').close()

# Environmental Specifications
num = 20  # number of agents
s = 3  # environment size in meters
total_checks = 0
num_apps = 20
total_interactions = 0
num_app_contacts = 0
start = time.time()

# Agent Parameters (play with these)
check_every = 0.1 #sec
k = 1.5
m = 2.0
t0 = 3
rad = .2  # Collision radius
sight_close = 0.5  # Neighbor search rang
sight_far = 1
maxF = 5  # Maximum force/acceleration

pixelsize = 1000
framedelay = 100
drawVels = True

win = Tk()
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
    print("Simulation of Agents on a flat 2D torus.")
    print("Agents avoid collisions using principles based on the laws of anticipation seen in human pedestrians.")
    print("Agents are white circles, Red agent moves faster.")
    print("Green Arrow is Goal Velocity, Red Arrow is Current Velocity")
    print("SPACE to pause, 'S' to step frame-by-frame, 'V' to turn the velocity display on/off.")
    print("")

    for i in range(num):
        circles.append(canvas.create_oval(0, 0, rad, rad, fill="white", tags = num))
        text.append(canvas.create_text(0, 0,fill="black",font="Times 15 italic bold",text=str(i+1)))
        velLines.append(canvas.create_line(0, 0, 10, 10, fill="red"))
        gvLines.append(canvas.create_line(0, 0, 10, 10, fill="green"))
        c.append(np.zeros(2))
        v.append(np.zeros(2))
        gv.append(np.zeros(2))
        c[i][0] = rnd.uniform(0, s)
        c[i][1] = rnd.uniform(0, s)
        ang = rnd.uniform(np.pi-0.2,np.pi+0.2) #moving to left
        v[i][0] = cos(ang)
        v[i][1] = sin(ang)

        gv[i] = 1.5 * np.copy(v[i])
        if i == 0:
            gv[i] *= 2
            canvas.itemconfig(circles[i], fill="#FAA")


def drawWorld():
    global rad, s
    for i in range(num):
        scale = pixelsize / s
        canvas.coords(circles[i], scale * (c[i][0] - rad), scale * (c[i][1] - rad), scale * (c[i][0] + rad),
                      scale * (c[i][1] + rad))
        canvas.coords(velLines[i], scale * c[i][0], scale * c[i][1], scale * (c[i][0] + 1. * rad * v[i][0]),
                      scale * (c[i][1] + 1. * rad * v[i][1]))
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
    global nbr, nd, c, contacts_close, contacts_far, total_interactions, num_app_contacts
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
            s2 = sight_close ** 2
            s3 = sight_far ** 2
            if l2 < s2:
                nbr[i].append(j)
                nd[i].append(sqrt(l2))
                if [j, i] not in contacts_close:
                    contacts_close.append([i, j])
                    total_interactions += 1
                    if j < num_apps and i < num_apps:
                        num_app_contacts += 1
            if l2 < s3 and l2 >= s2:
                if [j, i] not in contacts_far:
                    contacts_far.append([i, j])
                    total_interactions += 1
                    if j < num_apps and i < num_apps:
                        num_app_contacts += 1



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

    # if t < 10: print(t)

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
        # F.append(np.zeros(2))

        # vp = 1.4*v[i]/sqrt(v[i].dot(v[i]))
        F[i] += (gv[i] - v[i]) / .5
        F[i] += 1 * np.array([rnd.uniform(-1., 1.), rnd.uniform(-1., 1.)])

        for n, j in enumerate(nbr[i]):  # j is neighboring agent
            # if j < i: continue

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


    for i in range(num):
        a = F[i]
        v[i] += a * dt
        c[i] += v[i] * dt

        if c[i][0] < 0: c[i][0] = s  # wrap around for torus
        if c[i][1] < 0: c[i][1] = s
        if c[i][0] > s: c[i][0] = 0
        if c[i][1] > s: c[i][1] = 0


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
        elapsed_time = time.time() - start_time
        start_time = time.time()
        if not paused:
            # if ittr%100 == 0 : print ittr,"/",maxIttr
            update(0.02)
            ittr += 1
        drawWorld()
        if step == True:
            step = False
            paused = True

        win.title("Hallway Simulation - COVID Contact Tracing App")
        win.after(int(framedelay), drawFrame)
    if flag % int(check_every*1000//framedelay) == 0:
        total_checks += 1
        with open('../sim_output.txt', 'a') as output:
            output.write(f'Check Num (every {check_every} seconds): {total_checks}\n')
            output.write(f'Close Contacts: {len(contacts_close)}\n')
            for pair in contacts_close:
                output.write(f'{pair[0]} {pair[1]}\n')
            output.write(f'Far Contacts: {len(contacts_far)}\n')
            for pair in contacts_far:
                output.write(f'{pair[0]} {pair[1]}\n')
        with open('../apprelated/contactapp.txt', 'w') as output:
            output.write(f'Total Interactions (Close + Far): {total_interactions}\n')
            output.write(f'Total Contact Tracing Apps: {num_apps}\n')
            output.write(f'Total Interactions Traced by App: {num_app_contacts}\n')
            output.write(f'Percentage Interactions Traced by App: {round(num_app_contacts/total_interactions*100, 2)}%')
        print(f'check: {flag}')
        end = time.time()
        print(end-start)
    flag += 1

# win.on_resize=resize

win.bind("<space>", on_key_press)
win.bind("s", on_key_press)
win.bind("<Escape>", on_key_press)
win.bind("v", on_key_press)

initSim()
maxIttr = 5000

start_time = time.time()
win.after(framedelay, drawFrame)
mainloop()


