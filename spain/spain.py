import csv
# Data Snapshot sourced from: https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv

with open("owid-covid-data.csv") as fin:
    csv_reader = csv.reader(fin)
    with open("spain_weekly_snapshot.csv", "w") as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["location", "date", "total_cases", "total_deaths", "new_deaths"])
        for line in csv_reader:
            location = line[2]
            if location.lower() == "spain":
                date = line[3]
                total_cases = line[4]
                new_cases = line[5]
                total_deaths = line[7]
                new_deaths = line[8]
                csv_writer.writerow([location, date, total_cases, total_deaths, new_deaths])
