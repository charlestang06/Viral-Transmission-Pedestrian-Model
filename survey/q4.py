import csv

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
    q1A1q2A1 = 0
    q1A1q2A2 = 0
    q1A2q2A1 = 0
    q1A2q2A2 = 0
    for index in range(1, num_responses):
        if 'Yes' in q3[index]:
            q1A1 += 1
            if 'Yes' in q4[index]:
                q1A1q2A1 += 1
            if 'No' in q4[index]:
                q1A1q2A2 += 1
        elif 'No' in q3[index]:
            q1A2 += 1
            if 'Yes' in q4[index]:
                q1A2q2A1 += 1
            if 'No' in q4[index]:
                q1A2q2A2 += 1

    print(f'{school}: ')
    print(f'{round(float(q1A1q2A1*100/num_responses), 2)}% of people would allow the app to collect location data and were positive to sharing location data to health providers')
    print(f'{round(float(q1A1q2A2*100/num_responses), 2)}% of people would allow the app to collect location data and were negative to sharing location data to health providers')

    print(f'{round(float(q1A2q2A1*100/num_responses), 2)}% of people would not allow the app to collect location data and were positive to sharing location data to health providers')
    print(f'{round(float(q1A2q2A2*100/num_responses), 2)}% of people would not allow the app to collect location data and were negative to sharing location data to health providers')


correspondence('Public', 'Public_COVID-19 Contact Tracing Survey - Public_COVID-19 Contact Tracing Survey.csv')
correspondence('VT', 'VT_COVID-19 Contact Tracing Survey - VT_COVID-19 Contact Tracing Survey.csv')
correspondence('WPI', 'WPI_COVID-19 Contact Tracing Survey - WPI_COVID-19 Contact Tracing Survey.csv')