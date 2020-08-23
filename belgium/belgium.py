# belgium deaths by age: https://epistat.wiv-isp.be/covid/covid-19.html
# belgium population pyramid: https://www.populationpyramid.net/belgium/2020/

import csv

with open("belgium_population_june_30th.csv") as belgium:
    csv_belgium = [i for i in csv.reader(belgium)][1:]
    with open("mortality_rates_adjusted.csv") as mortalities:
        csv_mortality = [i for i in csv.reader(mortalities)][1:]

    with open("belgium_june_30th_datas.csv", "w") as output:
        csv_output = csv.writer(output)
        csv_output.writerow(["Age", "mortality", "population", "deaths", "infected", "seroprevalence"])
        for num1, num2 in zip(csv_belgium, csv_mortality):
            age = num1[0]
            population = int(num1[1])
            deaths = int(num1[2])
            mortality = float(num2[1])
            infected = deaths/mortality
            seroprevalence = infected/population
            csv_output.writerow([age, mortality, population, deaths, infected, seroprevalence])
