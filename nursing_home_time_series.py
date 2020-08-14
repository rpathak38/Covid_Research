import csv

with open("England_Wales_Nursing_Homes_Weekly_Snapshot") as nursing_homes:
    nursing_home_snapshot = [line for line in csv.reader(nursing_homes, delimiter="\t")]
    nursing_home_snapshot_sum = []

    for line in nursing_home_snapshot:
        try:
            date = line[0]
            care_home = int(line[1].replace(",",""))
            hospital = int(line[2].replace(",",""))
            elsewhere = int(line[3].replace(",",""))
        except ValueError:
            continue
        nursing_home_snapshot_sum.append((date, care_home+hospital+elsewhere))

    with open("England_Wales_Nursing_Homes_Time_Series.csv", "w") as nursing_home_time_series:
        csv_writer = csv.writer(nursing_home_time_series)

        csv_writer.writerow(("Date", "Total Nursing Home Dead"))
        total = 0
        for (date, num) in nursing_home_snapshot_sum:
            total = total+num
            csv_writer.writerow((date, total))
            print(date, total)