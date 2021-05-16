# TODO:Final
# 1. Check all outputs
# 2. Check for OTHER answers in the response
# 3. Check percentage using sub-groups in a different file?
# 4. Run this script with VT_response.csv

import csv

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
blank = []

with open('WPI_COVID-19 Contact Tracing Survey - WPI_COVID-19 Contact Tracing Survey.csv', 'r') as csvfile:
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

#	for row in reader:
#         if row[1] is None or row[1] == "":
#                 print(row[1])
#         else:

totalResp = len(q1)-1
print("\nTotal number of responses:", totalResp)

print("\nQ", q1[0])
Q1A1 = "Health authorities must perform contact tracing and participation is mandatory"
Q1A2 = "Health authorities must perform contact tracing and participation is voluntary"
Q1A3 = "Health authorities should not perform contact tracing"

Q1A1Index = []
Q1A2Index = []
Q1A3Index = []
Q1OtherIndex = []
for i in range(1, totalResp):
    if q1[i] == Q1A1:
        Q1A1Index.append(i)
    elif q1[i] == Q1A2:
        Q1A2Index.append(i)
    elif q1[i] == Q1A3:
        Q1A3Index.append(i)
    else:
        Q1OtherIndex.append(i)

countQ1A1 = len(Q1A1Index)
countQ1A2 = len(Q1A2Index)
countQ1A3 = len(Q1A3Index)
countQ1Other = len(Q1OtherIndex)
print("\tMandatory count:", countQ1A1, " Percentage:", countQ1A1 * 100 / totalResp)
print("\tVoluntary count:", countQ1A2, " Percentage:", countQ1A2 * 100 / totalResp)
print("\tNever count:", countQ1A3, " Percentage:", countQ1A3 * 100 / totalResp)
print("\tOther answers count", countQ1Other, " Percentage:", countQ1Other * 100 / totalResp)



print("\nQ", q2[0])
# More than one choice
Q2A1 = "Manual contact tracing: Healthcare workers perform contact tracing by interviewing you"
Q2A2 = "Digital contact tracing: Mobile phone performs contact tracing by electronically tracking you"
Q2A1A2 = "Manual contact tracing: Healthcare workers perform contact tracing by interviewing you;Digital contact tracing: Mobile phone performs contact tracing by electronically tracking you"
Q2A1Index = []
Q2A2Index = []
Q2A1A2Index = []
Q2OtherIndex = []
for i in range(1, totalResp):
    if q2[i] == Q2A1:
        Q2A1Index.append(i)
    elif q2[i] == Q2A2:
        Q2A2Index.append(i)
    elif Q2A1A2 in q2[i]:
        Q2A1A2Index.append(i)
    else:
        Q2OtherIndex.append(i)

countQ2A1 = len(Q2A1Index)
countQ2A2 = len(Q2A2Index)
countQ2A1A2 = len(Q2A1A2Index)
countQ2Other = len(Q2OtherIndex)

print("\tManual Public count:", countQ2A1, " Percentage:", countQ2A1 * 100 / totalResp)
print("\tDigital Public count:", countQ2A2, " Percentage:", countQ2A2 * 100 / totalResp)
print("\tBoth count:", countQ2A1A2, " Percentage:", countQ2A1A2 * 100 / totalResp)
print("\tOther answers count", countQ2Other, " Percentage:", countQ2Other * 100 / totalResp)

# manCT = 0; digCT = 0;
# for i in range(totalResp):
#        if q2[i].find(Q2A1):
#                manCT =  manCT+1
#        elif q2[i].find(Q2A2):
#                digCT = digCT+1
# print("\t ManCT count:",manCT)
# print("\t DigCT count:",digCT)

print("\nQ", q3[0])
# Yes or no question
Q3A1 = "Yes"
Q3A2 = "No"
Q3A1Index = []
Q3A2Index = []
Q3OtherIndex = []

for i in range(1, totalResp):
    if q3[i] == Q3A1:
        Q3A1Index.append(i)
    elif q3[i] == Q3A2:
        Q3A2Index.append(i)
    else:
        Q3OtherIndex.append(i)
countQ3A1 = len(Q3A1Index)
countQ3A2 = len(Q3A2Index)
countQ3Other = len(Q3OtherIndex)

print("\t", Q3A1, " count:", countQ3A1, " Percentage:", countQ3A1 * 100 / totalResp);
print("\t", Q3A2, " count:", countQ3A2, " Percentage:", countQ3A2 * 100 / totalResp);
print("\t Other answers count:", countQ3Other, " Percentage:", countQ3Other * 100 / totalResp);

print("\nQ", q4[0])
# Yes, Yes only anonymously, No, other question
Q4A1 = "Yes"
Q4A2 = "Yes, only anonymously"
Q4A3 = "No"
Q4A1Index = []
Q4A2Index = []
Q4A3Index = []
Q4OtherIndex = []

for i in range(1, totalResp):
    if q4[i] == Q4A1:
        Q4A1Index.append(i)
    elif q4[i] == Q4A2:
        Q4A2Index.append(i)
    elif q4[i] == Q4A3:
        Q4A3Index.append(i)
    else:
        Q4OtherIndex.append(i)
countQ4A1 = len(Q4A1Index)
countQ4A2 = len(Q4A2Index)
countQ4A3 = len(Q4A3Index)
countQ4Other = len(Q4OtherIndex)

print("\t", Q4A1, " count:", countQ4A1, " Percentage:", countQ4A1 * 100 / totalResp)
print("\t", Q4A2, " count:", countQ4A2, " Percentage:", countQ4A2 * 100 / totalResp)
print("\t", Q4A3, " count:", countQ4A3, " Percentage:", countQ4A3 * 100 / totalResp)
print("\t Other answers count:", countQ4Other, " Percentage:", countQ4Other * 100 / totalResp)

print("\nQ", q5[0])
# Yes, Yes only anonymously, No, other question
Q5A1 = "Yes"
Q5A2 = "Yes, only anonymously"
Q5A3 = "No"
Q5A1Index = []
Q5A2Index = []
Q5A3Index = []
Q5OtherIndex = []

for i in range(1, totalResp):
    if q5[i] == Q5A1:
        Q5A1Index.append(i)
    elif q5[i] == Q5A2:
        Q5A2Index.append(i)
    elif q5[i] == Q5A3:
        Q5A3Index.append(i)
    else:
        Q5OtherIndex.append(i)
countQ5A1 = len(Q5A1Index)
countQ5A2 = len(Q5A2Index)
countQ5A3 = len(Q5A3Index)
countQ5Other = len(Q5OtherIndex)

print("\t", Q5A1, " count:", countQ5A1, " Percentage:", countQ5A1 * 100 / totalResp)
print("\t", Q5A2, " count:", countQ5A2, " Percentage:", countQ5A2 * 100 / totalResp)
print("\t", Q5A3, " count:", countQ5A3, " Percentage:", countQ5A3 * 100 / totalResp)
print("\t Other answers count:", countQ5Other, " Percentage:", countQ5Other * 100 / totalResp)

print("\nQ", q6[0])
# More than one choice: Health Authorities, Health care providers, Private companies, General public, none, other
Q6A1 = "Health authorities"
Q6A1Index = []
Q6A2 = "Health care providers"
Q6A2Index = []
Q6A3 = "Private companies"
Q6A3Index = []
Q6A4 = "General public"
Q6A4Index = []
Q6A5 = "None"
Q6A5Index = []
Q6A1A2 = "Health authorities;Health care providers"
Q6A1A2Index = []
#newfromcharles
Q6A1A3 = "Health authorities;Private companies"
Q6A1A3Index = []
Q6A1A4 = "Health authorities;General public"
Q6A1A4Index = []
Q6A2A3 = "Health care providers;Private companies"
Q6A2A3Index = []
Q6A2A4 = "Health care providers;General public"
Q6A2A4Index = []
#newendfromcharles
Q6A1A2A3 = "Health authorities;Health care providers;Private companies"
Q6A1A2A3Index = []
Q6A1A2A4 = "Health authorities;Health care providers;General public"
Q6A1A2A4Index = []
Q6A1A2A3A4 = "Health authorities;Health care providers;Private companies;General public"
Q6A1A2A3A4Index = []
Q6OtherIndex = []

# more options - check the other index, has some 1-4 options with other answers too!
for i in range(1, totalResp):
    if q6[i] == Q6A1:
        Q6A1Index.append(i)
    elif q6[i] == Q6A2:
        Q6A2Index.append(i)
    elif q6[i] == Q6A3:
        Q6A3Index.append(i)
    elif q6[i] == Q6A4:
        Q6A4Index.append(i)
    elif q6[i] == Q6A5:
        Q6A5Index.append(i)
    elif q6[i] == Q6A1A2:
        Q6A1A2Index.append(i)
    elif q6[i] == Q6A1A2A3:
        Q6A1A2A3Index.append(i)
    elif q6[i] == Q6A1A2A4:
        Q6A1A2A4Index.append(i)
    elif q6[i] == Q6A1A2A3A4:
        Q6A1A2A3A4Index.append(i)
    elif q6[i] == Q6A1A3:
        Q6A1A3Index.append(i)
    elif q6[i] == Q6A1A4:
        Q6A1A4Index.append(i)
    elif q6[i] == Q6A2A3:
        Q6A2A3Index.append(i)
    elif q6[i] == Q6A2A4:
        Q6A2A3Index.append(i)
    else:
        Q6OtherIndex.append(i)

countQ6A1 = len(Q6A1Index)
countQ6A2 = len(Q6A2Index)
countQ6A3 = len(Q6A3Index)
countQ6A4 = len(Q6A4Index)
countQ6A5 = len(Q6A5Index)
countQ6A1A2 = len(Q6A1A2Index)
countQ6A1A3 = len(Q6A1A3Index)
countQ6A1A4 = len(Q6A1A3Index)
countQ6A2A3 = len(Q6A2A3Index)
countQ6A2A4 = len(Q6A2A4Index)
countQ6A1A2A3 = len(Q6A1A2A3Index)
countQ6A1A2A4 = len(Q6A1A2A4Index)
countQ6A1A2A3A4 = len(Q6A1A2A3A4Index)
countQ6Other = len(Q6OtherIndex)

print("\t", Q6A1, " count:", countQ6A1, " Percentage:", countQ6A1 * 100 / totalResp)
print("\t", Q6A2, " count:", countQ6A2, " Percentage:", countQ6A2 * 100 / totalResp)
print("\t", Q6A3, " count:", countQ6A3, " Percentage:", countQ6A3 * 100 / totalResp)
print("\t", Q6A4, " count:", countQ6A4, " Percentage:", countQ6A4 * 100 / totalResp)
print("\t", Q6A5, " count:", countQ6A5, " Percentage:", countQ6A5 * 100 / totalResp)
print("\t", Q6A1A2, " count:", countQ6A1A2, " Percentage:", countQ6A1A2 * 100 / totalResp)
print("\t", Q6A1A3, " count:", countQ6A1A3, " Percentage:", countQ6A1A3 * 100 / totalResp)
print("\t", Q6A1A4, " count:", countQ6A1A4, " Percentage:", countQ6A1A4 * 100 / totalResp)
print("\t", Q6A2A3, " count:", countQ6A2A3, " Percentage:", countQ6A2A3 * 100 / totalResp)
print("\t", Q6A2A4, " count:", countQ6A2A4, " Percentage:", countQ6A2A4 * 100 / totalResp)
print("\t", Q6A1A2A3, " count:", countQ6A1A2A3, " Percentage:", countQ6A1A2A3 * 100 / totalResp)
print("\t", Q6A1A2A4, " count:", countQ6A1A2A4, " Percentage:", countQ6A1A2A4 * 100 / totalResp)
print("\t", Q6A1A2A3A4, " count:", countQ6A1A2A3A4, " Percentage:", countQ6A1A2A3A4 * 100 / totalResp)
print("\t Other answers count:", countQ6Other, " Percentage:", countQ6Other * 100 / totalResp)

print("\nQ", q7[0])
Q7A1 = "Outdoor location data"
Q7A2 = "Indoor location data"
Q7A3 = "Location proximity to other app users"
Q7A1A2 = "Outdoor location data;Indoor location data"
Q7A1A3 = "Outdoor location data;Location proximity to other app users"
Q7A2A3 = "Indoor location data;Location proximity to other app users"
Q7A1A2A3 = "Outdoor location data;Indoor location data;Location proximity to other app users"

Q7A1Index = []
Q7A2Index = []
Q7A3Index = []
Q7A1A2Index = []
Q7A1A3Index = []
Q7A2A3Index = []
Q7A1A2A3Index = []
Q7OtherIndex = []

for i in range(1, totalResp):
    if q7[i] == Q7A1:
        Q7A1Index.append(i)
    elif q7[i] == Q7A2:
        Q7A2Index.append(i)
    elif q7[i] == Q7A3:
        Q7A3Index.append(i)
    elif q7[i] == Q7A1A2:
        Q7A1A2Index.append(i)
    elif q7[i] == Q7A1A3:
        Q7A1A3Index.append(i)
    elif q7[i] == Q7A2A3:
        Q7A2A3Index.append(i)
    elif q7[i] == Q7A1A2A3:
        Q7A1A2A3Index.append(i)
    else:
        Q7OtherIndex.append(i)

countQ7A1 = len(Q7A1Index)
countQ7A2 = len(Q7A2Index)
countQ7A3 = len(Q7A3Index)
countQ7A1A2 = len(Q7A1A2Index)
countQ7A1A3 = len(Q7A1A3Index)
countQ7A2A3 = len(Q7A2A3Index)
countQ7A1A2A3 = len(Q7A1A2A3Index)
countQ7Other = len(Q7OtherIndex)

print("\t", Q7A1, " count", countQ7A1, " Percentage:", countQ7A1 * 100 / totalResp)
print("\t", Q7A2, " count", countQ7A2, " Percentage:", countQ7A2 * 100 / totalResp)
print("\t", Q7A3, " count", countQ7A3, " Percentage:", countQ7A3 * 100 / totalResp)
print("\t", Q7A1A2, " count", countQ7A1A2, " Percentage:", countQ7A1A2 * 100 / totalResp)
print("\t", Q7A1A3, " count", countQ7A1A3, " Percentage:", countQ7A1A3 * 100 / totalResp)
print("\t", Q7A2A3, " count", countQ7A2A3, " Percentage:", countQ7A2A3 * 100 / totalResp)
print("\t", Q7A1A2A3, " count", countQ7A1A2A3, " Percentage:", countQ7A1A2A3 * 100 / totalResp)
print("\t Other answers count", countQ7Other, " Percentage:", countQ7Other * 100 / totalResp)

print("\nQ", q8[0])
Q8A1 = "A single number that reflects the likelihood of COVID-19 infection"
Q8A2 = "Locations of high risk contacts"
Q8A3 = "Date and time of high risk contacts"
Q8A1A2 = "A single number that reflects the likelihood of COVID-19 infection;Locations of high risk contacts"
Q8A1A3 = "A single number that reflects the likelihood of COVID-19 infection;Date and time of high risk contacts"
Q8A2A3 = "Locations of high risk contacts;Date and time of high risk contacts"
Q8A1A2A3 = "A single number that reflects the likelihood of COVID-19 infection;Locations of high risk contacts;Date and time of high risk contacts"

Q8A1Index = []
Q8A2Index = []
Q8A3Index = []
Q8A1A2Index = []
Q8A1A3Index = []
Q8A2A3Index = []
Q8A1A2A3Index = []
Q8OtherIndex = []

for i in range(1, totalResp):
    if q8[i] == Q8A1:
        Q8A1Index.append(i)
    elif q8[i] == Q8A2:
        Q8A2Index.append(i)
    elif q8[i] == Q8A3:
        Q8A3Index.append(i)
    elif q8[i] == Q8A1A2:
        Q8A1A2Index.append(i)
    elif q8[i] == Q8A1A3:
        Q8A1A3Index.append(i)
    elif q8[i] == Q8A2A3:
        Q8A2A3Index.append(i)
    elif q8[i] == Q8A1A2A3:
        Q8A1A2A3Index.append(i)
    else:
        Q8OtherIndex.append(i)

countQ8A1 = len(Q8A1Index)
countQ8A2 = len(Q8A2Index)
countQ8A3 = len(Q8A3Index)
countQ8A1A2 = len(Q8A1A2Index)
countQ8A1A3 = len(Q8A1A3Index)
countQ8A2A3 = len(Q8A2A3Index)
countQ8A1A2A3 = len(Q8A1A2A3Index)
countQ8Other = len(Q8OtherIndex)

print("\t", Q8A1, " count", countQ8A1, " Percentage:", countQ8A1 * 100 / totalResp)
print("\t", Q8A2, " count", countQ8A2, " Percentage:", countQ8A2 * 100 / totalResp)
print("\t", Q8A3, " count", countQ8A3, " Percentage:", countQ8A3 * 100 / totalResp)
print("\t", Q8A1A2, " count", countQ8A1A2, " Percentage:", countQ8A1A2 * 100 / totalResp)
print("\t", Q8A1A3, " count", countQ8A1A3, " Percentage:", countQ8A1A3 * 100 / totalResp)
print("\t", Q8A2A3, " count", countQ8A2A3, " Percentage:", countQ8A2A3 * 100 / totalResp)
print("\t", Q8A1A2A3, " count", countQ8A1A2A3, " Percentage:", countQ8A1A2A3 * 100 / totalResp)
print("\t Other answers count", countQ8Other, " Percentage:", countQ8Other * 100 / totalResp)

print("\nQ", q9[0])
Q9A1 = "Only me"
Q9A2 = "Health authority and me"
Q9A3 = "People I contacted, health authority, and me"

Q9A1Index = []
Q9A2Index = []
Q9A3Index = []
Q9OtherIndex = []

for i in range(1, totalResp):
    if q9[i] == Q9A1:
        Q9A1Index.append(i)
    elif q9[i] == Q9A2:
        Q9A2Index.append(i)
    elif q9[i] == Q9A3:
        Q9A3Index.append(i)
    else:
        Q9OtherIndex.append(i)

countQ9A1 = len(Q9A1Index)
countQ9A2 = len(Q9A2Index)
countQ9A3 = len(Q9A3Index)
countQ9Other = len(Q9OtherIndex)

print("\t", Q9A1, " count", countQ9A1, " Percentage:", countQ9A1 * 100 / totalResp)
print("\t", Q9A2, " count", countQ9A2, " Percentage:", countQ9A2 * 100 / totalResp)
print("\t", Q9A3, " count", countQ9A3, " Percentage:", countQ9A3 * 100 / totalResp)
print("\t Other answers count", countQ9Other, " Percentage:", countQ9Other * 100 / totalResp)

print("\nQ", q10[0])
Q10A1 = "At least once every day"
Q10A2 = "Once every two days"
Q10A3 = "Once every three days"
Q10A1A2 = "At least once every day;Once every two days"
Q10A1A3 = "At least once every day;Once every three days"
Q10A2A3 = "Once every two days;Once every three days"
Q10A1A2A3 = "At least once every day;Once every two days;Once every three days"


Q10A1Index = []
Q10A2Index = []
Q10A3Index = []
Q10A1A2Index = []
Q10A1A3Index = []
Q10A2A3Index = []
Q10A1A2A3Index = []
Q10OtherIndex = []

for i in range(1, totalResp):
    if q10[i] == Q10A1:
        Q10A1Index.append(i)
    elif q10[i] == Q10A2:
        Q10A2Index.append(i)
    elif q10[i] == Q10A3:
        Q10A3Index.append(i)
    elif q10[i] == Q10A1A2:
        Q10A1A2Index.append(i)
    elif q10[i] == Q10A2A3:
        Q10A2A3Index.append(i)
    elif q10[i] == Q10A1A3:
        Q10A1A3Index.append(i)
    elif q10[i] == Q10A1A2A3:
        Q10A1A2A3Index.append(i)
    else:
        Q10OtherIndex.append(i)

countQ10A1 = len(Q10A1Index)
countQ10A2 = len(Q10A2Index)
countQ10A3 = len(Q10A3Index)
countQ10A1A2 = len(Q10A1A2Index)
countQ10A1A3 = len(Q10A1A3Index)
countQ10A2A3 = len(Q10A2A3Index)
countQ10A1A2A3 = len(Q10A1A2A3Index)
countQ10Other = len(Q10OtherIndex)


print("\t", Q10A1, " count", countQ10A1, " Percentage:", countQ10A1 * 100 / totalResp)
print("\t", Q10A2, " count", countQ10A2, " Percentage:", countQ10A2 * 100 / totalResp)
print("\t", Q10A3, " count", countQ10A3, " Percentage:", countQ10A3 * 100 / totalResp)
print("\t", Q10A1A2, " count", countQ10A1A2, " Percentage:", countQ10A1A2 * 100 / totalResp)
print("\t", Q10A1A3, " count", countQ10A1A3, " Percentage:", countQ10A1A3 * 100 / totalResp)
print("\t", Q10A2A3, " count", countQ10A2A3, " Percentage:", countQ10A2A3 * 100 / totalResp)
print("\t", Q10A1A2A3, " count", countQ10A1A2A3, " Percentage:", countQ10A1A2A3 * 100 / totalResp)
print("\t Other answers count", countQ10Other, " Percentage:", countQ10Other * 100 / totalResp)

print("\nQ", q11[0])
Q11A1 = "Bluetooth"
Q11A2 = "WiFi"
Q11A3 = "Mobile data"
Q11A1A2 = "Bluetooth;WiFi"
Q11A1A3 = "Bluetooth;Mobile data"
Q11A2A3 = "WiFi;Mobile data"
Q11A1A2A3 = "Bluetooth;WiFi;Mobile data"

Q11A1Index = []
Q11A2Index = []
Q11A3Index = []
Q11A1A2Index = []
Q11A1A3Index = []
Q11A2A3Index = []
Q11A1A2A3Index = []
Q11OtherIndex = []

for i in range(1, totalResp):
    if q11[i] == Q11A1:
        Q11A1Index.append(i)
    elif q11[i] == Q11A2:
        Q11A2Index.append(i)
    elif q11[i] == Q11A3:
        Q11A3Index.append(i)
    elif q11[i] == Q11A1A2:
        Q11A1A2Index.append(i)
    elif q11[i] == Q11A1A3:
        Q11A1A3Index.append(i)
    elif q11[i] == Q11A2A3:
        Q11A2A3Index.append(i)
    elif q11[i] == Q11A1A2A3:
        Q11A1A2A3Index.append(i)
    else:
        Q11OtherIndex.append(i)
countQ11A1 = len(Q11A1Index)
countQ11A2 = len(Q11A2Index)
countQ11A3 = len(Q11A3Index)
countQ11A1A2 = len(Q11A1A2Index)
countQ11A1A3 = len(Q11A1A3Index)
countQ11A2A3 = len(Q11A2A3Index)
countQ11A1A2A3 = len(Q11A1A2A3Index)
countQ11Other = len(Q11OtherIndex)

print("\t", Q11A1, " count", countQ11A1, " Percentage:", countQ11A1 * 100 / totalResp)
print("\t", Q11A2, " count", countQ11A2, " Percentage:", countQ11A2 * 100 / totalResp)
print("\t", Q11A3, " count", countQ11A3, " Percentage:", countQ11A3 * 100 / totalResp)
print("\t", Q11A1A2, " count", countQ11A1A2, " Percentage:", countQ11A1A2 * 100 / totalResp)
print("\t", Q11A1A3, " count", countQ11A1A3, " Percentage:", countQ11A1A3 * 100 / totalResp)
print("\t", Q11A2A3, " count", countQ11A2A3, " Percentage:", countQ11A2A3 * 100 / totalResp)
print("\t", Q11A1A2A3, " count", countQ11A1A2A3, " Percentage:", countQ11A1A2A3 * 100 / totalResp)
print("\t Other answers count", countQ11Other, " Percentage:", countQ11Other * 100 / totalResp)

print("\nQ", q12[0])
Q12A1 = "Yes"
Q12A2 = "No"
Q12A3 = "Maybe"

Q12A1Index = []
Q12A2Index = []
Q12A3Index = []

for i in range(1, totalResp):
    if q12[i] == Q12A1:
        Q12A1Index.append(i)
    elif q12[i] == Q12A2:
        Q12A2Index.append(i)
    elif q12[i] == Q12A3:
        Q12A3Index.append(i)

countQ12A1 = len(Q12A1Index)
countQ12A2 = len(Q12A2Index)
countQ12A3 = len(Q12A3Index)
print("\t", Q12A1, " count", countQ12A1, " Percentage:", countQ12A1 * 100 / totalResp)
print("\t", Q12A2, " count", countQ12A2, " Percentage:", countQ12A2 * 100 / totalResp)
print("\t", Q12A3, " count", countQ12A3, " Percentage:", countQ12A3 * 100 / totalResp)

