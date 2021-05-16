import numpy as np
from math import sin, cos, sqrt, exp
import random as rnd
import time
import csv

#changeable
num_apps = 100
times = []
for x in range(0, 602):
    times.append(x/10)

time_counter = [0]*602

contact_time = 0 #sec

#do not change
check_every = 0.1 #sec
total_time = 0

short_app_contacts = 0
short_contacts = 0
short_far_contacts = 0
far_contacts = 0
far_app_contacts = 0

output =  open('sim_output.txt', 'r')
contents = output.readlines()

total_pairs = []
close_arr = []
close_count = []
far_arr = []
far_count = []
close = True

for x in range(len(contents)):
    contents[x] = contents[x].replace('\n', '')
for x in range(len(contents)):
    if 'Check Num' in contents[x]:
        continue
    elif 'Close Contacts' in contents[x]:
        close = True
        continue
    if close == True:
        temp = list(map(int, contents[x].split()))
        if temp in close_arr:
            close_count[close_arr.index(temp)] += 1
        elif [temp[1], temp[0]] in close_arr:
            close_count[close_arr.index([temp[1], temp[0]])] += 1
        else:
            close_arr.append(temp)
            if temp not in total_pairs or [temp[1], temp[0]] not in total_pairs:
                total_pairs.append(temp)
            close_count.append(1)

close_arr = [x for close_arr, x in sorted(zip(close_count, close_arr))]
close_count.sort()
close_arr.reverse()
close_count.reverse()


for x in range(len(close_arr)):
    if close_count[x]*check_every<contact_time:
        close_arr[x:] = []
        close_count[x:] = []
        break

open('time_output.txt', 'w').close()
with open('time_output.txt', 'w') as output:
    output.write(f'Short Close Contacts and Total Duration of Short Contact\n')
    for x in range(len(close_arr)):
        output.write(f'{close_arr[x][0]+1} {close_arr[x][1]+1} {round(close_count[x]*check_every, 2)} seconds\n')
        time_counter[times.index(round(close_count[x]*check_every, 2))] += 1
        total_time += round(check_every*close_count[x],2)

input = open('time_output.txt', 'r')
contents = input.readlines()
for x in range(len(contents)):
    contents[x] = contents[x].replace('\n', '')

with open('time_output.csv', 'w') as output:
    writer = csv.writer(output)
    writer.writerow(times)
    writer.writerow(time_counter)

with open('final_output.txt', 'a') as output:
    output.write(f'{len(total_pairs)} {round(total_time/len(total_pairs),3)}\n')

