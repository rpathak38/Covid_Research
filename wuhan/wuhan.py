import csv

with open("wuhan_data_lancet.csv") as wuhan:
    with open("spanish_mortality.csv") as mortalities:
        csv_mortalities = [i for i in csv.reader(mortalities)]
        csv_reader = [i for i in csv.reader(wuhan)]

        csv_reader = [i for i in zip(csv_reader[1:], csv_mortalities[1])]

        with open("wuhan_data_output.csv", "w") as output:
            csv_output = csv.writer(output)
            csv_output.writerow(["Age Group", "Dead", "Infected Estimate", "Infection Rate", "Infection Fatality Rate"])
            for data, mortality in csv_reader:
                age_group = data[0]
                deaths = int(data[1])
                population = int(data[2])
                mortality = float(mortality)

                try:
                    infected_estimate = deaths / mortality
                    infection_rate = infected_estimate/population
                    infection_fatality_rate = deaths/infected_estimate
                except ZeroDivisionError:
                    continue

                csv_output.writerow([age_group, deaths, infected_estimate, infection_rate, infection_fatality_rate])

