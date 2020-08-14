import csv
from matplotlib import pyplot as plt

# def plotter(net_mortality_distribution, nursing_home_distribution=None, date_of_data=None):
#     groups = []
#     dead_sums = []
#     for group, num_age, _, dead_sum in net_mortality_distribution:
#         groups.append(group)
#         dead_sums.append(int(dead_sum.replace(",", "")))
#
#     dead_sums_unedited = dead_sums.copy()
#
#     if nursing_home_distribution is not None:
#         title = "England and Wales COVID-19 Data June 12th"
#
#         for old_group, old_dead in nursing_home_distribution:
#             try:
#                 temp_index = groups.index(old_group)
#                 dead_sums[temp_index] = dead_sums[temp_index] - int(old_dead.replace(",", ""))
#             except ValueError:
#                 continue
#
#         plt.figure(1, figsize=(20, 10))
#         plt.title(title)
#         plt.plot(groups, dead_sums_unedited)
#         plt.plot(groups, dead_sums)
#         plt.legend(["Unfiltered Dead", "Nursing Homes Filtered"], loc='upper right')
#         plt.savefig('England_Wales_June_12.pdf')
#
#         # ratio development
#         plt.figure(2, figsize=(20, 10))
#         ratios = []
#         for (num, dead_sum) in enumerate(dead_sums):
#             ratio = dead_sum/ float(net_mortality_distribution[num][1].replace(",", ""))
#             ratios.append(ratio)
#
#         plt.figure(2, figsize=(20, 10))
#         plt.title("Ratio")
#         plt.plot(groups, ratios)
#         plt.legend(["Nursing Homes Filtered Dead Ratio"], loc='upper right')
#         plt.savefig('England_Wales_June_12_Ratio.pdf')
#
#         group_ratio_combined = list(zip(groups, ratios))
#         for group, number in group_ratio_combined:
#             print(group, number)
#
#         for i in range(len(group_ratio_combined)):
#             if i == 0:
#                 continue
#             try:
#                 print(group_ratio_combined[i][0]+",", group_ratio_combined[i][1]/group_ratio_combined[i-1][1])
#             except ZeroDivisionError:
#                 continue
#
#
#
#     else:
#         plt.figure(figsize=(20, 10))
#         title = "England and Wales COVID-19 Data {0}".format(date_of_data)
#         plt.title(title)
#         plt.plot(groups, dead_sums_unedited)
#         plt.savefig('England_Wales_{0}.pdf'.format(date_of_data))

# weekly snapshot data retrieved from: https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/deathsinvolvingcovid19englandandwales


date = input("Which date would you like to retrieve Covid-Death data for?")
with open("England_Wales_Age_Distribution", "r") as age_dist:
    with open("England_Wales_Weekly_Snapshot", "r") as weekly_snap:
        csv_read_age_dist = [i for i in csv.reader(age_dist, delimiter="\t")]

        csv_read_weekly_snap = [i for i in csv.reader(weekly_snap)]
        index = csv_read_weekly_snap[0].index(date)

        april_10_snap = [line[index] for line in csv_read_weekly_snap]

        with open("England_Wales_Time_Series", "r") as time_series:
            csv_read_time_series = [i for i in csv.reader(time_series)]
            april_10_sum = [line[index] for line in csv_read_time_series]

        mortality_dist = []
        zippy = zip(csv_read_age_dist, april_10_snap, april_10_sum)
        next(zippy)

        for (age, dead, sum_dead) in zippy:
            mortality_dist.append((age[0], age[1], dead, sum_dead))

        print("Age Group", "Population", "Weekly Snapshot Dead", "Cumulative Dead", "Ratio: Cumulative Dead/Population",
              sep=",")
        for age_group, population, snapshot_dead, cumulative_dead in mortality_dist:
            ratio = (float(cumulative_dead.replace(",", "")) / float(population.replace(",", ""))) * 100
            print(age_group, f'"{population}"', f'"{snapshot_dead}"', f'"{cumulative_dead}"', ratio, sep=",")

        for line in csv_read_age_dist:
            print(line)

        with open("England_Wales_June_12th_Nursing_Homes") as nursing_homes:
            csv_read_nursing_homes = csv.reader(nursing_homes)
            csv_read_nursing_homes = [line for line in csv_read_nursing_homes]

        nursing_home_dist = list(zip(csv_read_nursing_homes[0], csv_read_nursing_homes[1]))

        # plotter(mortality_dist, nursing_home_dist)

        # ratio stuff

        # names = []
        # ratios = []
        # integral_ratios = []
        # for name, age_num, dead, sum_dead in mortality_dist:
        #     names.append(name)
        #     ratio = float(dead.replace(",", "")) / float(age_num.replace(",", ""))
        #     ratios.append(ratio)
        #     integral_ratio = float(sum_dead.replace(",", "")) / float(age_num.replace(",", ""))
        #     integral_ratios.append(integral_ratio)
        #
        # plt.figure(figsize=(20, 5))
        # plt.subplot(1, 1, 1)
        # plt.title("England and Wales: COVID-19 Deaths/Age Distribution")
        # plt.plot(names, ratios)
        # plt.plot(names, integral_ratios)
        # plt.legend(["Snapshot", "Sum"], loc='upper right')
        # plt.savefig('England_Wales_April_3_Ratio.pdf', bbox_inches='tight')
        #
        # age_ratios = list(zip(names, ratios))

        # for i in range(len(age_ratios)):
        #     if i == 0:
        #         continue
        #     try:
        #         print(age_ratios[i][0]+",", age_ratios[i][1]/age_ratios[i-1][1])
        #     except ZeroDivisionError:
        #         continue
