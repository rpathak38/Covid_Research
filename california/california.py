import csv
import math

with open("california_covid_death_age_distribution") as fin:
    csv_reader = [line for line in csv.reader(fin)]
CALIFORNIA_POPULATION = 39557045

with open("california_adjusted_mortality") as mortalities:
    csv_mortalities = [i for i in csv.reader(mortalities)]


with open("california_data","w") as output:
    csv_output = csv.writer(output)
    csv_output.writerow(("Age", "Deaths", "Mortality Number", "Infected Estimate", "Population", "Infection Rate",
      "Infection Fatality Rate"))

    for line, mortality_data in zip(csv_reader[3:], csv_mortalities[3:]):
        age_group = line[0]
        cases = int(line[1].replace(",", ""))
        percent_cases = float(line[2])
        deaths = int(line[3].replace(",", ""))
        percent_deaths = float(line[4])

        percent_ca_population = float(line[5])
        population = (percent_ca_population / 100) * CALIFORNIA_POPULATION

        mortality_num = float(mortality_data[1])
        infected_estimate = deaths / mortality_num
        infection_rate = infected_estimate / population
        infection_fatality_rate = deaths / infected_estimate

        # temp = [age_group, deaths, mortality_num, infected_estimate, population, infection_rate,
        #         infection_fatality_rate]

        temp = [age_group, deaths, infected_estimate, infection_rate, infection_fatality_rate]
        csv_output.writerow(temp)

