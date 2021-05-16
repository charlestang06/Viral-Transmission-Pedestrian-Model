import csv

print("Correspondence: q9/q8")


def correspondence(school, file):
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []
    q11 = []
    q12 = []

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] is None or row[1] == "":
                print("Empty")
            else:
                q1.append(row[1])
                q2.append(row[2])
                q3.append(row[3])
                q4.append(row[4])
                q5.append(row[5])
                q6.append(row[6])
                q7.append(row[7])
                q8.append(row[8])
                q9.append(row[9])
                q10.append(row[10])
                q11.append(row[11])
                q12.append(row[12])

    num_responses = len(q1) - 1
    q1A1 = 0
    q1A2 = 0
    q1A3 = 0
    q1A1q2A1, q1A1q2A2, q1A1q2A3 = 0, 0, 0
    q1A2q2A1, q1A2q2A2, q1A2q2A3 = 0, 0, 0
    q1A3q2A1, q1A3q2A2, q1A3q2A3 = 0, 0, 0

    for index in range(1, num_responses):
        if 'me' in q9[index]:
            q1A1 += 1
            if 'A single number that reflects the likelihood of COVID-19 infection' in q8[index]:
                q1A1q2A1 += 1
            if 'Locations of high risk contacts' in q8[index]:
                q1A1q2A2 += 1
            if 'Date and time of high risk contacts' in q8[index]:
                q1A1q2A3 += 1
        if 'health authority' in q9[index].lower():
            q1A2 += 1
            if 'A single number that reflects the likelihood of COVID-19 infection' in q8[index]:
                q1A2q2A1 += 1
            if 'Locations of high risk contacts' in q8[index]:
                q1A2q2A2 += 1
            if 'Date and time of high risk contacts' in q8[index]:
                q1A2q2A3 += 1
        if 'People I contacted' in q9[index]:
            q1A3 += 1
            if 'A single number that reflects the likelihood of COVID-19 infection' in q8[index]:
                q1A3q2A1 += 1
            if 'Locations of high risk contacts' in q8[index]:
                q1A3q2A2 += 1
            if 'Date and time of high risk contacts' in q8[index]:
                q1A3q2A3 += 1

    if q1A1 == 0:
        q1A1 = 1
    if q1A2 == 0:
        q1A2 = 1
    if q1A3 == 0:
        q1A3 = 1

    print(f'{school}: ')
    print(f'{round(float(q1A1q2A1*100/num_responses), 2)}% of people believe they should be notified of their high risk contact and have app display a single number for prob. of COVID infection')
    print(f'{round(float(q1A1q2A2*100/num_responses), 2)}% of people believe they should be notified of their high risk contact and have app show locations of high COVID risk')
    print(f'{round(float(q1A1q2A3*100/num_responses), 2)}% of people believe they should be notified of their high risk contact and have app show dates/times of high COVID risk')

    print(f'{round(float(q1A2q2A1*100/num_responses), 2)}% of people believe health auth. should be notified of their high risk contact and have app display a single number for prob. of COVID infection')
    print(f'{round(float(q1A2q2A2*100/num_responses), 2)}% of people believe health auth. should be notified of their high risk contact and have app show locations of high COVID risk')
    print(f'{round(float(q1A2q2A3*100/num_responses), 2)}% of people believe health auth. should be notified of their high risk contact and have app show dates/times of high COVID risk')

    print(f'{round(float(q1A3q2A1*100/num_responses), 2)}% of people believe people they contacted should be notified of their high risk contact and have app display a single number for prob. of COVID infection')
    print(f'{round(float(q1A3q2A2*100/num_responses), 2)}% of people believe people they contacted should be notified of their high risk contact and have app show locations of high COVID risk')
    print(f'{round(float(q1A3q2A3*100/num_responses), 2)}% of people believe people they contacted should be notified of their high risk contact and have app show dates/times of high COVID risk')


correspondence('Public', 'Public_COVID-19 Contact Tracing Survey - Public_COVID-19 Contact Tracing Survey.csv')
correspondence('VT', 'VT_COVID-19 Contact Tracing Survey - VT_COVID-19 Contact Tracing Survey.csv')
correspondence('WPI', 'WPI_COVID-19 Contact Tracing Survey - WPI_COVID-19 Contact Tracing Survey.csv')