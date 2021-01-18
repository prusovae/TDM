import random
import string
import os

# Системный путь к справочникам (всегда одинаковый)
dict_path = os.path.join('data', 'dict')
# Наименования фалов справочников
# todo-low-prusove можно подумать, чтобы сделать универсальную функцию считывания для всех справочников из одной колонки
street_path = os.path.join(dict_path, 'streets.csv')
men_names_path = os.path.join(dict_path, 'men_names.csv')
women_names_path = os.path.join(dict_path, 'women_names.csv')
men_midnames_path = os.path.join(dict_path, 'men_midnames.csv')
women_midnames_path = os.path.join(dict_path, 'women_midnames.csv')
men_surnames_path = os.path.join(dict_path, 'men_surnames.csv')
women_surnames_path = os.path.join(dict_path, 'women_surnames.csv')
unisex_surnames_path = os.path.join(dict_path, 'unisex_surnames.csv')
phone_numbers_path = os.path.join(dict_path, 'phone_numbers.csv')
acct_chart_path = os.path.join(dict_path, 'acct_chart.csv')
currency_code_path = os.path.join(dict_path, 'currency_code.csv')

men_names_translit_path = os.path.join(dict_path, 'men_names_translit.csv')
women_names_translit_path = os.path.join(dict_path, 'women_names_translit.csv')
men_midnames_translit_path = os.path.join(dict_path, 'men_midnames_translit.csv')
women_midnames_translit_path = os.path.join(dict_path, 'women_midnames_translit.csv')
men_surnames_translit_path = os.path.join(dict_path, 'men_surnames_translit.csv')
women_surnames_translit_path = os.path.join(dict_path, 'women_surnames_translit.csv')
unisex_surnames_translit_path = os.path.join(dict_path, 'unisex_surnames_translit.csv')

streets = set()

men_names_translit = set()
women_names_translit = set()
men_midnames_translit = set()
women_midnames_translit = set()
men_surnames_translit = set()
women_surnames_translit = set()
unisex_surnames_translit = set()
person_surnames_translit = set()
person_names_translit = set()
person_midnames_translit = set()

men_names = set()
women_names = set()
men_names_list = list()
women_names_list = list()
men_midnames = set()
women_midnames = set()
men_midnames_list = list()
women_midnames_list = list()
men_surnames = set()
women_surnames = set()
unisex_surnames = set()
men_surnames_list = list()
women_surnames_list = list()
unisex_surnames_list = list()
phone_numbers = set()
person_surnames = set()
person_surnames_list = list()
person_names = set()
person_names_list = list()
person_midnames = set()
person_midnames_list = list()

acct_charts = set()
currency_codes = set()


def load_acct_chart(file_path):
    with open(file_path, encoding='utf-8') as file:
        for acct_chart in file:
            if acct_chart not in acct_charts:
                acct_charts.add(acct_chart.rstrip('\n'))


def load_phone_number(file_path):
    with open(file_path, encoding='utf-8') as file:
        for phone_number in file:
            if phone_number not in phone_numbers:
                phone_numbers.add(phone_number.rstrip('\n'))


def load_currency_code(file_path):
    with open(file_path, encoding='utf-8') as file:
        for currency_code in file:
            if currency_code not in currency_codes:
                currency_codes.add(currency_code.rstrip('\n'))


def load_datamasking_dicts():
    # Загружаем в память справочник ФИО
    load_person_names()
    load_person_surnames()
    load_person_midnames()
    # Загружаем в память справочник ФИО в транслите
    load_person_names_translit()
    load_person_surnames_translit()
    load_person_midnames_translit()
    # Загружаем в память справочник адресов
    load_streets()
    # Загружаем в память справочник (план счетов)
    load_acct_chart(acct_chart_path)
    # Загружаем в память справочник (коды валют)
    load_currency_code(currency_code_path)
    # Загружаем в память справочник (телефонные номера)
    load_phone_number(phone_numbers_path)


def load_streets():
    with open(street_path, encoding='utf-8') as file:
        for street in file:
            if street not in streets:
                streets.add(street.rstrip('\n'))

def load_person_names():
    # заполняем системные справочники имен
    with open(men_names_path, encoding='utf-8') as f:
        for name in f:
            men_names_list.append(name.rstrip('\n'))
            person_names_list.append(name.rstrip('\n'))
    with open(women_names_path, encoding='utf-8') as f:
        for name in f:
            women_names_list.append(name.rstrip('\n'))
            person_names_list.append(name.rstrip('\n'))

def load_person_names_translit():
    # заполняем системные справочники имен
    with open(men_names_translit_path, encoding='utf-8') as f:
        for name in f:
            men_names_translit.add(name.rstrip('\n'))
            person_names_translit.add(name.rstrip('\n'))
    with open(women_names_translit_path, encoding='utf-8') as f:
        for name in f:
            women_names_translit.add(name.rstrip('\n'))
            person_names_translit.add(name.rstrip('\n'))


def load_person_surnames():
    # заполняем системные справочники фамилий
    with open(unisex_surnames_path, encoding='utf-8') as f:
        for surname in f:
            unisex_surnames_list.append(surname.rstrip('\n'))
            person_surnames_list.append(surname.rstrip('\n'))
    with open(men_surnames_path, encoding='utf-8') as f:
        for surname in f:
            men_surnames_list.append(surname.rstrip('\n'))
            person_surnames_list.append(surname.rstrip('\n'))
    with open(women_surnames_path, encoding='utf-8') as f:
        for surname in f:
            women_surnames_list.append(surname.rstrip('\n'))
            person_surnames_list.append(surname.rstrip('\n'))


def load_person_surnames_translit():
    # заполняем системные справочники фамилий
    with open(unisex_surnames_translit_path, encoding='utf-8') as f:
        for surname in f:
            unisex_surnames_translit.add(surname.rstrip('\n'))
            person_surnames_translit.add(surname.rstrip('\n'))
    with open(men_surnames_translit_path, encoding='utf-8') as f:
        for surname in f:
            men_surnames_translit.add(surname.rstrip('\n'))
            person_surnames_translit.add(surname.rstrip('\n'))
    with open(women_surnames_translit_path, encoding='utf-8') as f:
        for surname in f:
            women_surnames_translit.add(surname.rstrip('\n'))
            person_surnames_translit.add(surname.rstrip('\n'))


def load_person_midnames():
    with open(men_midnames_path, encoding='utf-8') as f:
        for midname in f:
            men_midnames_list.append(midname.rstrip('\n'))
            person_midnames_list.append(midname.rstrip('\n'))
    with open(women_midnames_path, encoding='utf-8') as f:
        for midname in f:
            women_midnames_list.append(midname.rstrip('\n'))
            person_midnames_list.append(midname.rstrip('\n'))


def load_person_midnames_translit():
    with open(men_midnames_translit_path, encoding='utf-8') as f:
        for midname in f:
            men_midnames_translit.add(midname.rstrip('\n'))
            person_midnames_translit.add(midname.rstrip('\n'))
    with open(women_midnames_translit_path, encoding='utf-8') as f:
        for midname in f:
            women_midnames_translit.add(midname.rstrip('\n'))
            person_midnames_translit.add(midname.rstrip('\n'))


# todo-medium-asyunov сделать синхронную выборку ФИО либо женского либо мужского (пока только мужские ФИО)
# todo-medium-asyunov обсудить, и возможно сделать и list и set для ФИО, чтобы каждый раз не приводить к list
def get_random_person_name():
    return random.choice(men_names_list).capitalize()
    #return 'masked_get_random_person_name'

def get_random_person_surname():
    return random.choice(men_surnames_list).capitalize()
    #return 'masked_get_random_person_surname'

def get_random_person_midname():
    return random.choice(men_midnames_list).capitalize()
    #return 'masked_get_random_person_midname'
# todo-medium-aprusov оптимизировать эти волосы работает в 1000 раз дольше других функций
def get_random_person_fio():
    #return get_random_person_surname() + ' ' + get_random_person_name() + ' ' + get_random_person_midname()
    return 'masked_get_random_person_fio'

def get_random_person_inn():
    return random.randrange(100000000000, 999999999999)


def get_random_org_inn():
    return random.randrange(1000000000, 9999999999, 1)


def get_random_kpp():
    return random.randrange(100000000, 999999999, 1)


def get_random_email():
    letters = string.ascii_lowercase
    random_email = ''.join(random.choice(letters) for i in range(random.randrange(1, 20, 1))) \
                   + "@" \
                   + ''.join(random.choice(letters) for i in range(random.randrange(1, 7, 1))) \
                   + "." \
                   + ''.join(random.choice(letters) for i in range(random.randrange(2, 4, 1)))
    return random_email


def get_random_phone_number():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random_phone_number = ''.join('+7(') \
                          + ''.join(random.choice(letters) for i in range(3)) \
                          + ''.join(')') \
                          + ''.join(random.choice(letters) for i in range(3)) \
                          + ''.join('-') \
                          + ''.join(random.choice(letters) for i in range(2)) \
                          + ''.join('-') \
                          + ''.join(random.choice(letters) for i in range(2))
    return random_phone_number


def get_random_ogrn():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random_ogrn = ''.join(random.choice(letters[:-1])) \
                  + ''.join(random.choice(letters) for i in range(12))
    return random_ogrn


def get_random_okpo():  # пока не понятно, нужно ли это (отдельно не считается перс данными)
    pass


def get_random_org_name():
    company_type = ['ООО', 'ЗАО', 'ОАО', 'ПАО', 'АО', 'Товарищество', 'Производственный кооператив',
                    'Фермерское хозяйство', 'Общественная организация', 'Политическая организация',
                    'Религиозная организация', 'Профсоюз', 'Партия']
    roots = ['Пром', 'Интер', 'Бор', 'Газ', 'Нефть', 'Мяс', 'Гос', 'Капитал', 'Груп', 'Сталь', 'Проект', 'Баш', 'Сиб',
             'Прод', 'Куб', 'Мос', 'Граждан', 'Проект', 'Кабель', 'Юг', 'Монтаж', 'Строй', 'Девелопмент', 'Теле', 'Ком',
             'Рыб', 'Краб', 'Рак', 'Металл', 'Чермет', 'Цвет', 'Бетон', 'Удар', 'Лом', 'Кирка']
    org_name = ''.join(random.choice(company_type) + ' "' + ''.join(
        random.choice(roots) for i in range(random.randrange(2, 6, 1)))) + '"'
    return org_name


def get_random_rus_passport():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random_passport = ''.join(random.choice(letters) for i in range(2)) \
                      + ''.join(' ') \
                      + ''.join(random.choice(letters) for i in range(2)) \
                      + ''.join(' ') \
                      + ''.join(random.choice(letters) for i in range(6))
    return random_passport


def get_random_rus_driver_license():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    rus_driver_license = ''.join(random.choice(letters) for i in range(2)) \
                         + ''.join(' ') \
                         + ''.join(random.choice(letters) for i in range(2)) \
                         + ''.join(' ') \
                         + ''.join(random.choice(letters) for i in range(6))
    return rus_driver_license


def get_random_card_number():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    pay_system = ['2', '3', '4', '5', '6', '7']
    card_number = ''.join(random.choice(pay_system) \
                          + ''.join(random.choice(letters) for i in range(5)) \
                          + ''.join(random.choice(letters) for i in range(9)) \
                          + ''.join(random.choice(letters)))
    return card_number


# todo-high-aprusov срочно переделай этот кусок говна на справочник
def get_random_account_number():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    account_second_order = ["10207", "99997"]
    currency_code = ["392"]
    account_number = ''.join(random.choice(account_second_order)) \
                     + ''.join(random.choice(currency_code)) \
                     + ''.join(random.choice(letters) for i in range(12))
    return account_number


def get_random_street():
    return random.choice(list(streets))


def get_random_foreign_passport():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    foreign_passport = ''.join(random.choice(letters) for i in range(2)) \
                       + ''.join(' ') \
                       + ''.join(random.choice(letters) for i in range(7))
    return foreign_passport


def get_random_foreign_driver_license():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    foreign_driver_license = ''.join(random.choice(letters) for i in range(2)) \
                             + ''.join(' DD ') \
                             + ''.join(random.choice(letters) for i in range(6))
    return foreign_driver_license


def get_random_person_snils():
    letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    person_snils = ''.join(random.choice(letters) for i in range(3)) \
                   + ''.join('-') \
                   + ''.join(random.choice(letters) for i in range(3)) \
                   + ''.join('-') \
                   + ''.join(random.choice(letters) for i in range(3)) \
                   + ''.join(' ') \
                   + ''.join(random.choice(letters) for i in range(2))
    return person_snils


domain_func_mapping = dict()
domain_func_mapping['person_name'] = get_random_person_name
domain_func_mapping['person_midname'] = get_random_person_midname
domain_func_mapping['person_surname'] = get_random_person_surname
domain_func_mapping['person_fio'] = get_random_person_fio
domain_func_mapping['person_inn'] = get_random_person_inn
domain_func_mapping['org_inn'] = get_random_org_inn
domain_func_mapping['kpp'] = get_random_kpp
domain_func_mapping['email'] = get_random_email
domain_func_mapping['phone_number'] = get_random_phone_number
domain_func_mapping['org_name'] = get_random_org_name
domain_func_mapping['ogrn'] = get_random_ogrn
domain_func_mapping['rus_passport'] = get_random_rus_passport
domain_func_mapping['foreign_passport'] = get_random_foreign_passport
domain_func_mapping['rus_driver_license'] = get_random_rus_driver_license
domain_func_mapping['foreign_driver_license'] = get_random_foreign_driver_license
domain_func_mapping['card_number'] = get_random_card_number
domain_func_mapping['account_number'] = get_random_account_number
domain_func_mapping['street'] = get_random_street
domain_func_mapping['person_snils'] = get_random_person_snils

# todo-low-aprusov разметить статус по доменам, для каких доменов какие функции готовы...
'''
Методы идентификации доменов
1. Машинное обучение
    - mobile_num
2. Справочники
    - person_name
    - person_midname
    - person_surname
    - person_birth_cert
    - street
    - city
3. Регулярные выражения
    - person_inn
    - person_snils
    - org_inn
    - org_name
    - kpp
    - email
    - ogrn
    - okpo (?)
    - rus_passport
    - foreign_passport
    - rus_driver_license
    - foreign_driver_license
    - acct_num
    - card_num
    - address
'''
