import csv
with open("../cfr_ifr_table/owid-covid-data.csv") as database:
    csv_reader = csv.reader(database)
    for