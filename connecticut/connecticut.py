import csv

# Covid 19 deaths by age group: https://data.ct.gov/Health-and-Human-Services/COVID-19-Cases-and-Deaths-by-Age-Group/ypz6-8qyf

with open("COVID-19_Cases_and_Deaths_by_Age_Group.csv") as fin:
    csv_reader = csv.reader(fin)

    date = input(
        "For which date would you like Covid Death data for in Connecticut? Please enter your request as: mm/dd/yyyy")

    date_data = []
    for (index, line) in enumerate(csv_reader):
        if index == 0:
            date_data.append(line)
        if line[0] == date:
            date_data.append(line)

    date_data_filtered = []
    for line in date_data:
        age = line[1]
        total_deaths = line[6]
        date_data_filtered.append((age, total_deaths))

    mortality = []
    with open("mortality") as mortality_fin:
        csv_mortality = csv.reader(mortality_fin)
        for line in csv_mortality:
            mortality.append(line)
    mortality = list(zip(mortality[0], mortality[1]))

    with open("age_distribution") as age_distribution:
        csv_age_dist = [i for i in csv.reader(age_distribution)]
        age_dist = list(zip(csv_age_dist[0], csv_age_dist[1]))

    with open("connecticut_data", "w") as output:
        csv_output = csv.writer(output)

        categories = ["Age Group", "Deaths", "Mortality", "Estimated Infected", "Population", "Estimated "
                                                                                              "Infection "
                                                                                              "Rate",
                      "Infection Fatality Rate"]
        print(categories)
        csv_output.writerow(categories)

        for mortalities, deaths, distribution in zip(mortality[2:9], date_data_filtered[3:10], age_dist[2:8]):
            age = mortalities[0]
            mortality_num = mortalities[1]
            death = deaths[1]
            population = distribution[1]
            population = int(population.replace(",", ""))
            infected_estimate = float(death) / float(mortality_num)
            infection_rate = infected_estimate / population
            infection_fatality_rate = float(death) / float(infected_estimate)

            temp = [age, death, mortality_num, infected_estimate, population, infection_rate, infection_fatality_rate]
            print(temp)
            csv_output.writerow(temp)

# with open("COVID-19_Cases_and_Deaths_by_Age_Group.csv") as stuff:
#     csv_stuff = csv.reader(stuff)
#     death = 0
#     for line in csv_stuff:
#         if line[0] == date:
#             deaths = int(line[6].replace(",", ""))
#             death = death + deaths
#             print(line)
#     print(death)
#
# with open("age_distribution") as ages:
#     csv_ages = [line for line in csv.reader(ages)]
#     totals = 0
#     for num in csv_ages[1]:
#         totals = totals + int(num.replace(",", ""))
#
# print(float(death)/float(totals*0.05))

