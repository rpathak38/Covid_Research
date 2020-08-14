import csv


def integral(list_deaths):
    integral_list = []
    for i in range(2):
        integral_list.append(list_deaths[i])

    list_indexes = enumerate(list_deaths)
    next(list_indexes)
    next(list_indexes)

    for (index, num) in list_indexes:
        prev_sum = adjacent_sum(integral_list, list_deaths, index)
        integral_list.append(prev_sum)

    return integral_list


def adjacent_sum(integral_list, list_deaths, index):
    behind = int(integral_list[index - 1])
    try:
        current = int(list_deaths[index])
    except ValueError:
        current = int(list_deaths[index].replace(",", ""))
    finally:
        return behind + current


if __name__ == "__main__":
    with open("England_Wales_Weekly_Snapshot", "r") as filein:
        csv_read = csv.reader(filein)
        with open("England_Wales_Time_Series", "w") as fileout:
            csv_write = csv.writer(fileout)
            csv_read = [i for i in csv_read]

            print(csv_read[0])
            csv_write.writerow(csv_read[0])

            csv_read = iter(csv_read)
            next(csv_read)

            for line in csv_read:
                integral_list = integral(line)
                print(integral_list)
                csv_write.writerow(integral_list)
