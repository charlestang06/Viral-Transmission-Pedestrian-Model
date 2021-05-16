vars = open('variables.txt', 'r')
contents = vars.readlines()
contents[0] = list(map(float, contents[0].split()))

open('lazy.csv').close()

# Environmental Specifications
iterations = int(contents[0][4])

with open('final_output.txt', 'r') as output:
    content = output.readlines()
    final_1 = []
    final_2 = []
    final_3 = []
    final_4 = []
    for x in range(iterations+1):
        final_1.append([0 for i in range(13)])
        final_2.append([0 for i in range(13)])
        final_3.append([0 for i in range(13)])
        final_4.append([0 for i in range(13)])
    curr_column = 0
    curr_row  = 0
    for line in range(len(content)):
        if line % iterations == 0:
            curr_column += 1
            curr_row = 0
        temp = content[line].split()
        final_1[curr_row][curr_column] = temp[0]
        final_2[curr_row][curr_column] = temp[1]
        final_3[curr_row][curr_column] = temp[2]
        final_4[curr_row][curr_column] = temp[3]
        curr_row += 1

file = open('lazy.csv', 'w')
import csv
wr = csv.writer(file, lineterminator='\n')
for x in final_1:
    wr.writerow(x)
wr.writerow([])
for x in final_2:
    wr.writerow(x)
wr.writerow([])
for x in final_3:
    wr.writerow(x)
wr.writerow([])
for x in final_4:
    wr.writerow(x)