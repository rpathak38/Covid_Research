import csv

with open("COVID-19_Cases_Summarized_by_Age_Group.csv") as fin:
    csv_reader = csv.reader(fin)
    age_distribution = set()

    for line in csv_reader:
        print(line)
        age_distribution.add(line[1])

print(age_distribution)