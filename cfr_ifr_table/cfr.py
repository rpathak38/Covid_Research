import csv

with open("owid-covid-data.csv") as data:
    csv_reader = csv.reader(data)

    i=0
    for line in csv_reader:
        (iso_code, continent, location, date, total_cases, new_cases, total_deaths, new_deaths, total_cases_per_million, new_cases_per_million, total_deaths_per_million, new_deaths_per_million, total_tests, new_tests, total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, tests_units, stringency_index, population, population_density, median_age, aged_65_older, aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence, female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy) = line
        if i == 0:
            print(date, total_cases, total_deaths)
            i = i+1
        if location == "Sweden":
            print(date, total_cases, total_deaths)

