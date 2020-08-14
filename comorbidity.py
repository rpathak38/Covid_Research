import csv
import numpy as np
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def series_maker(start="6-Mar-20", end="3-Jul-20"):
    with open("England_Wales_Weekly_Snapshot") as snapshot:
        csv_reader = [line for line in csv.reader(snapshot)]
        start_index = csv_reader[0].index(start)
        end_index = csv_reader[0].index(end)

        totals = []
        for line in csv_reader[1:]:
            total = 0
            for i in range(start_index, end_index + 1):
                total = total + int(line[i].replace(",", ""))
            totals.append(total)

        return totals


def forty_five_ninety_nine(age_distribution):
    total = 0
    for i in range(10):
        total = total + int(age_distribution[i])
    age_distribution_fixed = [total]

    for i in age_distribution[10:]:
        age_distribution_fixed.append(i)
    age_groups = ["0-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90+"]

    age_distribution_fixed = {key: value for key, value in zip(age_groups, age_distribution_fixed)}
    return age_distribution_fixed


march_june_age_dist = forty_five_ninety_nine(series_maker())

with open("England and Wales Comorbities by Age.csv") as comorbities:
    csv_reader = csv.reader(comorbities)

    conditions = defaultdict(dict)
    # dictionary with all main pre-existing conditions as keys, values are lists with distribution of ages that
    # contain has tuples
    # e.g AIDS, [(0-44, 90), (45-49, 30)]

    for (_, __, ___, age, condition, deaths) in csv_reader:
        conditions[condition][age] = deaths

    ages_list = ["0-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90+"]
    conditions = [(key, value) for key, value in conditions.items() if key != "Main pre-existing condition"]
    x = np.array(range(len(list(conditions))))
    y = np.array(range(len(ages_list)))
    xpos, ypos = np.meshgrid(x, y)

    # base positions defined
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    z = np.zeros((len(x), len(y)))

    i = 0
    for condition, ages in conditions:
        j = 0
        for age in ages:
            if ages.get(age) is None:
                z[i][j] = None
            else:
                if int(ages.get(age).replace(",", "")) <1000:
                    z[i][j] = int(ages.get(age).replace(",", ""))
                else:
                    z[i][j] = 0
            j = j + 1
        i = i + 1

    # deltas
    dx = np.ones_like(xpos)
    dy = dx.copy()
    dz = z.flatten()

    #labels

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection="3d")

    # ax.set_xticks(range(len(conditions)))
    # temp = [condition[0] for condition in conditions]
    # for i in temp:
    #     print(i)
    # ax.set_xticklabels(temp)
    # ax.set_xlabel("Conditions", labelpad=7)

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    plt.show()

    with open("comorbidity.csv", "w") as finout:
        csv_writer = csv.writer(finout)
        csv_writer.writerow(["Condition", *ages_list])
        for condition, ages in conditions[1:]:
            temp = []
            for age in ages_list:
                num = ages.get(age)
                if num is not None:
                    temp.append(num)
                else:
                    temp.append(0)
            csv_writer.writerow([condition, *temp])






    # conditions = [(key, value) for key, value in conditions.items()]
    #
    #
    #
    # diagram = np.zeros((len(conditions) - 1, len(ages_list)), np.uint32)
    #
    # i = 0
    # for condition, ages in conditions:
    #     j = 0
    #     for age, deaths in ages.items():
    #         try:
    #             index = ages_list.index(age)
    #             diagram[i][index] = int(deaths.replace(",", ""))
    #         except ValueError:
    #             print(condition, age, deaths)
    #             i = i - 1
    #         finally:
    #             j = j + 1;
    #     i = i + 1
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1, projection='3d')
    #
    # for index, z in np.ndenumerate(diagram):
    #     if z > 0:
    #         ax.scatter(index[0], index[1], z, c='red')
    #         ax.plot3D(index[0], index[1], z, c='red')
    #
    # plt.show()

    # Todo: Develop a 3-dimensional graph of the conditions, ages, deaths
