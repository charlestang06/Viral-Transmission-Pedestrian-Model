import winsound, os, subprocess, sys, numpy as np, time, random, math, scipy

open('processing files/final_output.txt', 'w').close() #clear output files
sizes = [2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30]

#Environment Variables
num_agents = 100
num_apps = 10 #first num_community agents in clusters have contact apps
min_contact_time = 0

velocity = 1
hallway = 1 #0 = false, 1 = true

iterations = 1

frac_of_circ = 32
community_range = 5
num_community = 20


cluster = True #True if want to run with community clusters, False if want to run normal simulation
two_hallway = True

for size in sizes:
    for x in range(iterations):
        if num_agents > 100 and size==2.5:
            continue
        if size != 15:
            continue
        else:
            with open('processing files/variables.txt', 'w') as output: #initiate environment variables
                output.write(f'{num_agents} {size} {velocity} {hallway} {iterations} {frac_of_circ} {community_range} {num_community} {num_apps} {min_contact_time}')
            if cluster == True and two_hallway == False:
                os.system('python cluster.py') #runs the simulation with clusters/community
            elif two_hallway == True and cluster == True:
                os.system('python twowayhallway.py')
            else:
                os.system('python varysize.py') #runs the simulation without clusters/commuinties
            if cluster == True:
                os.system('python cluster-timecalc.py') #processes data from sim_output for clustered
            else:
                os.system('python timecalc.py') #processes data from the sim_output for non-clustered

if cluster == True:
    os.system('python cluster-lazy.py')
else:
    os.system('python lazy.py') #convert final_output to csv

winsound.Beep(440,500)