import csv
response_dates = []
#ex. 2020/10/23 9:28:55 PM AST
with open('VT_COVID-19 Contact Tracing Survey - VT_COVID-19 Contact Tracing Survey.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] is None or row[1] == "" or row[0] == "Timestamp":
            print("Empty")
        else:
            response_dates.append(row[0])
for x in range(len(response_dates)):
    temp = response_dates[x]
    response_dates[x] = temp[5:10]

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_track = [10, 11, 12, 1, 2]

dates = []


for x in month_track:
    for y in range(1, months[x-1]+1):
        if x < 10:
            if y < 10:temp = f'0{x}/0{y}'
            else:temp = f"0{x}/{y}"
        else:
            if y<10:temp = f'{x}/0{y}'
            else:temp = f'{x}/{y}'
        dates.append(temp)

num_responses = [0]*len(dates)
for x in range(len(response_dates)):
    index_ = dates.index(response_dates[x])
    num_responses[index_] += 1

file = open('datecounter_output.csv', 'w')
wr = csv.writer(file, lineterminator='\n')
wr.writerow(dates)
wr.writerow(num_responses)

