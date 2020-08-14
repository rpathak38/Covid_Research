import csv

with open("new_york_state_covid_dead_age_distribution") as fin:
    csv_reader = [line for line in csv.reader(fin)]

    date_data = list(zip(csv_reader[0], csv_reader[1]))

    #mortality is referenced from spanish paper as a ratio
    mortality = []
    with open("/Users/rishi-mac/PycharmProjects/Covid_Research/connecticut/mortality") as mortality_fin:
        csv_mortality = csv.reader(mortality_fin)
        for line in csv_mortality:
            mortality.append(line)
    mortality = list(zip(mortality[0], mortality[1]))

    with open("new_york_state_population_age_distribution") as age_distribution:
        csv_age_dist = [i for i in csv.reader(age_distribution)]
        age_dist = list(zip(csv_age_dist[0], csv_age_dist[1]))

    with open("mew_york_state_data", "w") as output:
        csv_output = csv.writer(output)

        categories = ["Age Group", "Deaths", "Mortality", "Estimated Infected", "Population", "Estimated "
                                                                                              "Infection "
                                                                                              "Rate",
                      "Estimated Infection Fatality Rate"]
        print(categories)
        csv_output.writerow(categories)

        infected = 0
        death = 0

        for mortalities, deaths, distribution in zip(mortality[2:], date_data[2:], age_dist[2:]):
            age = mortalities[0]
            mortality_num = mortalities[1]
            death = deaths[1].replace(",","")
            population = distribution[1]
            population = int(population.replace(",", ""))
            infected_estimate = float(death) / float(mortality_num)
            infection_rate = infected_estimate / population
            infection_fatality_rate = float(death) / float(infected_estimate)

            temp = [age, death, mortality_num, infected_estimate, population, infection_rate, infection_fatality_rate]
            print(temp)
            csv_output.writerow(temp)

