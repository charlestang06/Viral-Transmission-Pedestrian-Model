import winsound, os, subprocess, sys, numpy as np, time, random, math

os.chdir('C:\\Users\charl\PycharmProjects\\research')

open('processing/final_output.txt', 'w').close() #clear output files
sizes = [5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30]

#Environment Variables
num_agents = 100
num_apps = 0 #first num_community agents in clusters have contact apps
min_contact_time = 0
contact_radius = 2.5
velocity = 1
scenario = 1#0 = room, 1 = one-way, 2 = two-way
iterations = 5

#cluster envirionment variables
frac_of_circ = 32
community_range = 10
num_community = 0
cluster = False #True if want to run with community clusters, False if want to run normal simulation


for size in sizes:
    for x in range(iterations):
        print(size)
        print(x+1)
        os.chdir('C:\\Users\\charl\\PycharmProjects\\research')
        with open('processing/variables.txt', 'w') as output: #initiate environment variables
            output.write(f'{num_agents} {size} {velocity} {scenario} {iterations} {frac_of_circ} {community_range} {num_community} {num_apps} {min_contact_time} {contact_radius}')
        if cluster == True and scenario != 2:
            os.system('python cluster.py') #runs the simulation with clusters/community
        elif scenario == 2 and cluster == False:
            os.system('python twowayhallway.py')
        else:
            os.system('python varysize.py') #runs the simulation without clusters/commuinties
        if cluster == True:
            os.chdir('C:\\Users\\charl\\PycharmProjects\\research\\processing')
            os.system('python cluster-timecalc.py') #processes data from sim_output for clustered
        else:
            os.chdir('C:\\Users\\charl\\PycharmProjects\\research\\processing')
            os.system('python timecalc.py') #processes data from the sim_output for non-clustered

if cluster == True:
    os.system('python cluster-lazy.py')
else:
    os.system('python lazy.py') #convert final_output to csv

print('All Done :)')
winsound.Beep(440,500)
