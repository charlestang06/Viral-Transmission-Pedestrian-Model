num_apps = 0
short_app_contacts = 0
short_contacts = 0
short_far_contacts = 0
far_contacts = 0
far_app_contacts = 0

input = open('../processing files/time_output.txt', 'r')
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
            if int(temp[0]) < num_apps and int(temp[1]) < num_apps:
                short_app_contacts += 1
            short_contacts += 1
        elif isClose == False:
            if int(temp[0]) < num_apps and int(temp[1]) < num_apps:
                far_app_contacts += 1
            far_contacts += 1

if short_contacts == 0:
    short_contacts = 1000000
if far_contacts == 0:
    far_contacts = 1000000
print(f'Percentage of Close Contacts Traced: {round(short_app_contacts*100/short_contacts, 2)}%')
print(f'Percentage of Far Contacts Traced: {round(far_app_contacts*100/far_contacts, 2)}%')