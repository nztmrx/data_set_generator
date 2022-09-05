import random
import uuid
import multiprocessing


def generate_fio_dr():
    with open('data_sets/male_names_rus.txt', encoding='utf-8', newline='') as f:
        male_name = f.read().split()

    with open('data_sets/male_surnames_rus.txt', encoding='utf-8', newline='') as f:
        male_surname = f.read().split()

    with open('data_sets/female_names_rus.txt', encoding='utf-8', newline='') as f:
        female_names = f.read().split()

    gender = random.randint(1, 2)
    dr = generate_date()

    if gender == 1:
        gender = 'М'

        name = male_name[random.randrange(1, len(male_name))]
        sur_name = male_surname[random.randrange(1, len(male_surname))] + 'джеметр'
        male_patronymic = male_name[random.randrange(1, len(male_name))] + 'ичь'

        return name, sur_name, male_patronymic, dr, gender

    elif gender == 2:
        gender = 'Ж'

        female_name = female_names[random.randrange(1, len(female_names))]
        female_surname = male_surname[random.randrange(1, len(male_surname))] + 'аяджеметр'
        female_patronymic = male_name[random.randrange(1, len(male_name))] + 'овна'

        return female_name, female_surname, female_patronymic, dr, gender


def generate_dudl():
    dudl_rg_kod = random.randrange(1, 99)
    if dudl_rg_kod < 10:
        dudl_rg_kod = f"0{dudl_rg_kod}"

    dudl_get_year = str(random.randrange(1970, 2022))
    dudl_get_year_cut = dudl_get_year[2:]

    """ FINAL DATA """

    dudl_type = random.randrange(1, 27)
    dudl_seria = str(dudl_rg_kod) + str(dudl_get_year_cut)
    dudl_number = [str(random.randrange(1, 9)) for i in range(6)]
    dudl_number = ''.join(dudl_number)
    dudl_start_date = f"{dudl_get_year}-{generate_date(year=False, day=True, month=True)}"
    dudl_end_date = f"{int(dudl_get_year) + 20}-{generate_date(year=False, month=True, day=True)}"
    where_dudl_gets = f"ТЕСТОВЫМ ОТДЕЛЕНИЕМ УФМС РОССИИ ПО ГОР. МОСКВЕ ПО РАЙОНУ ЭЛЕМЕНТ"
    dudl_kod_where_get = dudl_rg_kod
    civil = "РФ"
    is_civil = False

    fio_dr_gender = generate_fio_dr()
    name = fio_dr_gender[0]
    surname = fio_dr_gender[1]
    patronymic = fio_dr_gender[2]
    dr = fio_dr_gender[3]
    sex = fio_dr_gender[4]

    born_city = "Москва"
    born_county = "Россия"

    status = "ACTIVE"
    a = f"{dudl_type}, {dudl_seria}, {dudl_number}, {dudl_start_date}, {dudl_end_date}," \
        f"{where_dudl_gets}, {dudl_kod_where_get}, {civil}, {is_civil}, {name}, {surname}," \
        f" {patronymic}, {dr}, {sex}, {born_city}, {born_county}, {status}"

    return a


def generate_date(year=True, month=True, day=True):
    if year == False and month == True and day == True:
        month = random.randrange(1, 12)
        date = random.randrange(1, 31)

        if date < 10:
            date = f"0{date}"
        if month < 10:
            month = f"0{month}"

        return f"{month}-{date}"

    pc_year = random.randrange(1990, 2022)
    pc_month = random.randrange(1, 12)
    pc_date = random.randrange(1, 31)

    if pc_date < 10:
        pc_date = f"0{pc_date}"
    if pc_month < 10:
        pc_month = f"0{pc_month}"

    return f"{pc_year}-{pc_month}-{pc_date}"


def generate_policy_type():
    policy_types = ['П', 'В', 'Э', 'C', 'Х', 'К']

    return ''.join(random.sample(policy_types, 1))


def generate_random_enp(len_value=16):
    a = [str(random.randrange(1, 9)) for i in range(len_value)]
    a = ''.join(a)
    return a


def generate_pcy():
    pcy_number = [str(random.randrange(1, 9)) for _ in range(16)]
    pcy_number = ''.join(pcy_number)

    pcy_seria = [str(random.randrange(1, 9)) for _ in range(11)]
    pcy_seria = ''.join(pcy_seria)

    enp = f"{generate_random_enp()}"
    data = generate_fio_dr()

    pcyDateB = "2022-09-02"
    pcyDateE = "2022-09-02"
    pcyDateH = "2022-09-02"
    pcyDateT = "2022-09-02"
    pcyDateEnpCalc = "2022-09-02"
    pcyDatePr = "2022-09-02"
    policy_type = f"{generate_policy_type()}"
    pcyStatus = "ACTIVE"
    descr = "TEST_DESCR"
    gender = data[4]
    insurId = uuid.uuid4()
    insurfId = insurId
    name = data[0]
    surname = data[1]
    patronymic = data[2]
    dr = data[3]
    gender = data[4]

    return f"{pcy_seria}, {pcy_number}, {enp}, {pcyDateB}, {pcyDateE}, {pcyDateH}, {pcyDateT}, {pcyDateEnpCalc}, {pcyDatePr}, {policy_type}, {pcyStatus}, {descr}, {gender}, {insurId}, {insurfId}, {name}, {surname}, {patronymic}, {dr}, {gender}"


def generate_sn():
    snils = [str(random.randrange(1, 9)) for _ in range(11)]
    snils.insert(3, '-')
    snils.insert(7, '-')
    snils.insert(-2, '-')
    snils = ''.join(snils)
    descr = 'Тестовый комент'
    dsourceType = "CS"


generate_sn()


def random_data_set(count, csv_count):
    result = []
    for i in range(count + 1):
        ter = '77'
        ern = [str(random.randrange(1, 9)) for _ in range(8)]
        ern = ''.join(ern)
        print()

        result.append(f"{ter}, {generate_pcy()}, {generate_dudl()}, {ern}, {generate_sn()}'\n")

        print(f"[$={csv_count}][SS={i}")

    result = ''.join(result)
    with open(f'result{csv_count}.csv', 'a') as f:
        f.write(result)


def main():
    p1 = multiprocessing.Process(target=random_data_set, args=(100000, 1))
    p1.start()

    p2 = multiprocessing.Process(target=random_data_set, args=(100000, 2))
    p2.start()

    p3 = multiprocessing.Process(target=random_data_set, args=(100000, 3))
    p3.start()

    p4 = multiprocessing.Process(target=random_data_set, args=(100000, 4))
    p4.start()

    p5 = multiprocessing.Process(target=random_data_set, args=(100000, 5))
    p5.start()


if __name__ == "__main__":
    main()
