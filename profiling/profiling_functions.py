import re

import numpy as np
import pandas as pd

from masking.lingvo_functions import get_word_in_1st_lang_form
from masking.masking_functions import person_surnames, person_names, person_midnames, streets, phone_numbers, \
    person_surnames_translit, person_names_translit, person_midnames_translit
from masking.masking_functions import currency_codes, acct_charts
# from joblib import load

# Загрузка модели ИИ
# clf = load('z:\\target_address.joblib')

# Функция, которая подготавливает данные для модели ML
def prepare_data(df):
    #переводим текст в lower формат, удаляем пробелы слева, справа и удаляем все множественные пробелы
    #df['txt']=df['txt'].str.lower().str.strip().str.replace(' +', ' ')
    df['len']=df.txt.str.len()
    df['digits_len'] = df.txt.str.count('[0-9]')
    df['alpha_len'] = df.txt.str.count('[A-Za-zА-Яа-яЁё]')
    df['dot_len']=df.txt.str.count('\.')
    df['space_len']=df.txt.str.count(' ')
    df['dash_len']=df.txt.str.count('\-')
    df['plus_len']=df.txt.str.count('\+')
    df['comma_len']=df.txt.str.count(',')
    df['bracket']=df.txt.str.count('[()]')
    df = df.drop(['txt'], axis=1)
    return df

def is_surname(in_string):
    if str(in_string).lower() in person_surnames:
        result = True
    else:
        result = False
    return result


def is_surname_translit(in_string):
    if str(in_string).lower() in person_surnames_translit:
        result = True
    else:
        result = False
    return result


def is_surname_in_lang_form(in_string):
    # переводим слово в именительный падеж и проверяем в справочнике
    word_in_1st_lang_form, lang_form = get_word_in_1st_lang_form(str(in_string))
    return is_surname(word_in_1st_lang_form)


def is_name(in_string):
    if str(in_string).lower() in person_names:
        result = True
    else:
        result = False
    return result


def is_name_translit(in_string):
    if str(in_string).lower() in person_names_translit:
        result = True
    else:
        result = False
    return result


def is_midname(in_string):
    if str(in_string).lower() in person_midnames:
        result = True
    else:
        result = False
    return result


def is_midname_translit(in_string):
    if str(in_string).lower() in person_midnames_translit:
        result = True
    else:
        result = False
    return result


def is_street(in_string):
    if str(in_string).lower() in streets:
        result = True
    else:
        result = False
    return result


def is_email(string):
    pattern = '\A[a-z0-9!#$%&*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?'
    email = re.findall(pattern, str(string).strip(' '))
    return bool(email)

# todo low prusovae сделать функцию поиска номера паспорта
# todo-low-aprusov продумать потом для разных длин карт
def is_card_number(string):
    if string.isdigit() and len(string) == 16:
        card_num = list(str(string.strip(' ')))
        discharge_weighty = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
        checksum = int()
        new_string = ([int(x) * int(discharge_weighty) for x, discharge_weighty in zip(card_num, discharge_weighty)])
        for i in new_string:
            if int(i) > 9:
                i = int(i) - 9
            checksum += int(i)
        # Если остаток = 0, то номер карты верен
        return not bool(checksum % 10)
    else:
        return False


def is_account_number(string):
    l_string = str(string)
    if l_string.isdigit() and len(l_string) == 20:
        return bool(l_string[5:8] in currency_codes and l_string[0:5] in acct_charts)
    else:
        return False


def is_person_fio(in_string):
    l_string = str(in_string).strip().lower()
    pattern = '^[А-Яа-яЁё]+ [А-Яа-яЁё]+ [А-Яа-яЁё]+$'
    result = re.findall(pattern, l_string)
    if (bool(result)) and (l_string[-3:] in ['вич', 'вна']):
        return True
    else:
        return False


# def get_address_pct(s):
#     df = pd.DataFrame()
#     df['txt'] = s
#     df = prepare_data(df)
#     df['new'] = predictions = (clf.predict_proba(df)[:, 1])
#     return df['new'].mean()


def is_address(in_string):
    new_string = in_string.replace('.', ' ')
    new_string = new_string.replace(',', ' ')
    new_string = new_string.replace('улица', 'ул')
    if 'ул ' in new_string:
        return True
    else:
        return False


def is_rus_passport(in_string):
    l_string = str(in_string).strip().lower()
    serial_rus = 'серия'
    number_rus = 'номер'
    serial_eng = 'serial'
    number_eng = 'number'
    pattern = '^([0-9]{2}\s{1}[0-9]{2}\s{1}[0-9]{6})|([0-9]{2}[0-9]{2}\s{1}[0-9]{6})' \
              '|(' + serial_rus + '\s{1}[0-9]{2}\s{1}[0-9]{2}\s{1}' + number_rus + '\s{1}[0-9]{6})' \
              '|(' + serial_rus + '\s{1}[0-9]{2}[0-9]{2}\s{1}' + number_rus + '\s{1}[0-9]{6})' \
              '|(' + serial_eng + '\s{1}[0-9]{2}\s{1}[0-9]{2}\s{1}' + number_eng + '\s{1}[0-9]{6})' \
              '|(' + serial_eng + '\s{1}[0-9]{2}[0-9]{2}\s{1}' + number_eng + '\s{1}[0-9]{6})'
    rus_passport = re.fullmatch(pattern, l_string)
    return bool(rus_passport)


def is_phone_number(in_string):
    phone = [int(s) for s in in_string if s.isdigit()]
    if len(phone) != 0 and phone[0] in [7, 8]:
        return bool(len(phone) == 11)
    else:
        return False


def is_org_inn(in_string):
    if in_string.isdigit() and len(in_string) == 10:
        org_inn = list(str(in_string.strip(' ')))
        discharge_weighty = [2, 4, 10, 3, 5, 9, 4, 6, 8]
        checksum = int()
        new_string = ([int(x) * int(discharge_weighty) for x, discharge_weighty in zip(org_inn[:-1], discharge_weighty)])
        for i in new_string:
            checksum+=i
        control_digit = (checksum-((checksum//11)*11))
        check_digit = int(org_inn[-1])
        if control_digit > 9:
            return bool(control_digit % 10 == check_digit)
        else:
            return bool(control_digit == check_digit)
    return False


def is_person_inn(in_string):
    if in_string.isdigit() and len(in_string) == 12:
        person_inn = list(str(in_string.strip(' ')))
        discharge_weighty = [7,2,4,10,3,5,9,4,6,8,0]
        checksum = int()
        new_string = ([int(x) * int(discharge_weighty) for x, discharge_weighty in zip(person_inn[:-1], discharge_weighty)])
        for i in new_string:
            checksum+=i
        control_digit = checksum % 11
        if control_digit > 9:
            return bool(control_digit % 10 == control_digit)
        else:
            return bool(control_digit == control_digit)
    return False


def is_org_name(in_string):
    #'ООО', 'ЗАО', 'ОАО', 'ПАО', 'АО''
    if 'ооо ' in in_string:
        return True
    elif 'ао ' in in_string:
        return True
    else:
        return False


def define_domain(in_series):
    result_dict = dict()
    max_score = 0
    domain_prefix = ''
    # todo-low-prusove ниже из колонки удаляются null. Это будет не нужно когда Жека допишет функцию get1000notnullrows
    # nan получается когда импортируем пустые данные из csv и преобразуем в текст
    s = in_series.replace('nan', np.nan).dropna()
    # none получается, когда импортируем из IQ поля, в которых null
    s = s.replace('none', np.nan).dropna()
    # пустые строки получаются когда импортируем пустые строки из IQ, так как ''!=null
    s = s.replace('^$', np.nan, regex=True).dropna()
    # если массив при этом не закончился, то выполняем код
    if len(s) > 0:
        result_dict[s.map(lambda x: is_person_fio(x)).mean()] = domain_prefix + 'person_fio'
        result_dict[s.map(lambda x: is_org_name(x)).mean()] = domain_prefix + 'org_name'
        result_dict[s.map(lambda x: is_phone_number(x)).mean()] = domain_prefix + 'phone_number'
        result_dict[s.map(lambda x: is_rus_passport(x)).mean()] = domain_prefix + 'rus_passport'
        result_dict[s.map(lambda x: is_address(x)).mean()] = domain_prefix + 'address'

        if s.str.count(' ').mean() >= 1:
            # если в среднем пробелом больше одного в строке, значит тип комплексный
            domain_prefix = 'complex_'
            # все значения строк поместим в set
            l_temp_set = set(s)
            # формируем единый лист из всех слов во всех строках в этой колонке
            l_temp_list = ' '.join(l_temp_set).split(' ')
            # удаляем все слова длиной меньше 4 символов
            for word in l_temp_list:
                if len(word) < 4:
                    l_temp_list.remove(word)
            # формируем новый столбец, более длинный, чем тот который был на входе, но зато только из 1 слова
            new_series = pd.Series(l_temp_list)
            # в отличие от простого поля, в этом нам нужно искать фамилии учитывая падеж
            result_dict[new_series.map(lambda x: is_surname_in_lang_form(x)).mean()] = domain_prefix + 'person_surname'
            result_dict[new_series.map(lambda x: is_phone_number(x)).mean()] = domain_prefix + 'phone_number'
        else:
            new_series = s
            # а тут падеж искать не будем
            result_dict[new_series.map(lambda x: is_surname(x)).mean()] = domain_prefix + 'person_surname'

        result_dict[new_series.map(lambda x: is_name(x)).mean()] = domain_prefix + 'person_name'
        result_dict[new_series.map(lambda x: is_midname(x)).mean()] = domain_prefix + 'person_midname'
        result_dict[new_series.map(lambda x: is_name_translit(x)).mean()] = domain_prefix + 'person_name_translit'
        result_dict[new_series.map(lambda x: is_midname_translit(x)).mean()] = domain_prefix + 'person_midname_translit'
        result_dict[new_series.map(lambda x: is_surname_translit(x)).mean()] = domain_prefix + 'person_surname_translit'
        result_dict[new_series.map(lambda x: is_street(x)).mean()] = domain_prefix + 'street'
        result_dict[new_series.map(lambda x: is_email(x)).mean()] = domain_prefix + 'email'
        result_dict[new_series.map(lambda x: is_account_number(x)).mean()] = domain_prefix + 'account_number'
        result_dict[new_series.map(lambda x: is_card_number(x)).mean()] = domain_prefix + 'card_number'
        result_dict[new_series.map(lambda x: is_org_inn(x)).mean()] = domain_prefix + 'org_inn'
        result_dict[new_series.map(lambda x: is_person_inn(x)).mean()] = domain_prefix + 'person_inn'
        max_score = max(list(result_dict.keys()))

    if max_score >= 0.01:
        return result_dict[max_score], max_score
    else:
        return '', 1

