import numpy as np
from math import sin, cos, sqrt, exp
import random as rnd
import time
#changeable
num_apps = 100

contact_time = 0 #sec

#do not change
check_every = 0.1 #sec

total_time = 0


short_app_contacts = 0
short_contacts = 0
short_far_contacts = 0
far_contacts = 0
far_app_contacts = 0

output =  open('../processing/sim_output.txt', 'r')
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
    elif 'Far Contacts' in contents[x]:
        close = False
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
    elif close == False:
        temp = list(map(int, contents[x].split()))
        if temp in far_arr:
            far_count[far_arr.index(temp)] += 1
        elif [temp[1], temp[0]] in far_arr:
            far_count[far_arr.index([temp[1], temp[0]])] += 1
        else:
            far_arr.append(temp)
            far_count.append(1)
            if temp not in total_pairs or [temp[1], temp[0]] not in total_pairs:
                total_pairs.append(temp)

close_arr = [x for close_arr, x in sorted(zip(close_count, close_arr))]
close_count.sort()
far_arr = [x for far_arr, x in sorted(zip(far_count, far_arr))]
far_count.sort()

close_arr.reverse()
close_count.reverse()
far_arr.reverse()
far_count.reverse()

for x in range(len(close_arr)):
    if close_count[x]*check_every<contact_time:
        close_arr[x:] = []
        close_count[x:] = []
        break


for x in range(len(far_arr)):
    if far_count[x]*check_every<contact_time:
        far_arr[x:] = []
        far_count[x:] = []
        break

open('../processing/time_output.txt', 'w').close()
with open('../processing/time_output.txt', 'w') as output:
    output.write(f'Short Close Contacts and Total Duration of Short Contact\n')
    for x in range(len(close_arr)):
        output.write(f'{close_arr[x][0]+1} {close_arr[x][1]+1} {round(close_count[x]*check_every, 2)} seconds\n')
        total_time += round(check_every*close_count[x],2)
    output.write('Far Close Contacts and Total Duration of Far Contact\n')
    for x in range(len(far_arr)):
        output.write(f'{far_arr[x][0]+1} {far_arr[x][1]+1} {round(far_count[x]*check_every, 2)} seconds\n')
        total_time += round(check_every * far_count[x], 2)


input = open('../processing/time_output.txt', 'r')
contents = input.readlines()
for x in range(len(contents)):
    contents[x] = contents[x].replace('\n', '')

isClose = True
for x in range(len(contents)):
    temp = contents[x].split()
    if 'Short Contact' in contents[x]:
        isClose = True
    elif 'Far Contact' in contents[x]:
        isClose = False
    else:
        if isClose == True:
            temp.remove('seconds')
            if int(temp[0]) < num_apps+1 and int(temp[1]) < num_apps+1:
                short_app_contacts += 1
            short_contacts += 1
        elif isClose == False:
            if int(temp[0]) < num_apps+1 and int(temp[1]) < num_apps+1:
                far_app_contacts += 1
            far_contacts += 1

if short_contacts == 0:
    short_contacts = 10000000
if far_contacts == 0:
    far_contacts = 10000000

print(f'Percentage of Close Contacts Traced with {num_apps} apps and {contact_time} seconds contact time: {round(short_app_contacts*100/short_contacts, 2)}%')
print(f'Percentage of Far Contacts Traced with {num_apps} apps and {contact_time} seconds contact time: {round(far_app_contacts*100/far_contacts, 2)}%')
print(f'Avg Contact Time: {round(total_time/len(total_pairs),3)}')
