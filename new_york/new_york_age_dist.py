import csv

with open("Sheet 2-Table 1.csv") as fin:
    csv_reader = csv.reader(fin)

    population = 0
    output = []
    for group, number in csv_reader:
        if group == "All Ages":
            population = float(number.replace(",", ""))
        output.append((group, (float(number.replace(",", "")) / population)*100))

    with open("new_york_percentage.csv", "w") as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(("Age Group", "Percentage"))
        for line in output:
            csv_writer.writerow(line)
