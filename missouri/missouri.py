# Missouri Deaths by age: https://web.archive.org/web/20200530040543/http://mophep.maps.arcgis.com/apps/MapSeries/index.html?appid=8e01a5d8d8bd4b4f85add006f9e14a9d
# Missouri Population by age: https://censusreporter.org/profiles/04000US29-missouri/

import csv

with open("missouri_population_may30th.csv") as belgium:
    csv_belgium = [i for i in csv.reader(belgium)][1:]
    with open("mortality_rates_adjusted.csv") as mortalities:
        csv_mortality = [i for i in csv.reader(mortalities)][1:]

    with open("missouri_may_30th_datas.csv", "w") as output:
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