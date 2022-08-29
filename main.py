import random

from Tools.scripts.finddiv import process


def random_data_set(count):

    with open('data_sets/male_names_rus.txt', encoding='utf-8', newline='') as f:
        male_name = f.read().split()

    with open('data_sets/male_surnames_rus.txt', encoding='utf-8', newline='') as f:
        male_surname = f.read().split()

    with open('data_sets/female_names_rus.txt', encoding='utf-8', newline='') as f:
        female_names = f.read().split()
    # print(len(male_name))

    for i in range(count + 1):
        gender = random.randint(1, 2)

        result = []

        date_of_dr = random.randrange(1, 31)
        month_of_dr = random.randrange(1, 12)
        year_of_dr = random.randint(1950, 2022)

        if date_of_dr < 10:
            date_of_dr = f"0{date_of_dr}"
        if month_of_dr < 10:
            month_of_dr = f"0{month_of_dr}"

        dr = f"{date_of_dr}.{month_of_dr}.{year_of_dr}"
        print(dr)
        if gender == 1:
            gender = 'муж.'

            name = male_name[random.randrange(1, len(male_name))]
            sur_name = male_surname[random.randrange(1, len(male_surname))] + 'джеметр'
            male_patronymic = male_name[random.randrange(1, len(male_name))] + 'ичь'

            result.append(f"{name}, {sur_name}, {male_patronymic}, {dr}, {gender}\n")

        elif gender == 2:
            gender = 'жен.'

            female_name = female_names[random.randrange(1, len(female_names))]
            female_surname = male_surname[random.randrange(1, len(male_surname))] + 'аяджеметр'
            female_patronymic = male_name[random.randrange(1, len(male_name))] + 'овна'

            result.append(f"{female_name}, {female_surname}, {female_patronymic}, {dr}, {gender}\n")

            # print(result)

        with open('result.csv', 'a') as f:
            f.write(str(*result))


def main():
    random_data_set(1000000)


if __name__ == "__main__":
    main()
