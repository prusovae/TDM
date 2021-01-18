import os
import json

surname_lang_forms_in_path = os.path.join('data', 'lang_forms', 'surname_lang_forms_in.json')
surname_lang_forms_out_path = os.path.join('data', 'lang_forms', 'surname_lang_forms_out.json')
surname_lang_forms_in = dict()
surname_lang_forms_out = dict()


def load_lang_forms():
    # Загружаем в память окончания разных падежей фамилий и их соответствия с фамилиями
    load_surname_lang_forms_in(surname_lang_forms_in_path)
    load_surname_lang_forms_out(surname_lang_forms_out_path)


def load_surname_lang_forms_in(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        temp_dict = dict(json.load(json_file))
        for el in temp_dict:
            surname_lang_forms_in[el] = temp_dict[el]


def load_surname_lang_forms_out(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        temp_dict = dict(json.load(json_file))
        for el in temp_dict:
            surname_lang_forms_out[el] = temp_dict[el]


def get_word_in_1st_lang_form(in_string):
    lang_form = 'I'
    result = in_string
    surname_ending = ''
    # ищем окончания фамилий из 4 букв
    if in_string[-4:] in surname_lang_forms_in:
        surname_ending = in_string[-4:]
    # ищем окончания фамилий из 3 букв
    elif in_string[-3:] in surname_lang_forms_in:
        surname_ending = in_string[-3:]
    if surname_ending != '':
        # строчка ниже заменяет окончание слова на окончание в именительном падеже
        result = surname_lang_forms_in[surname_ending]['I'].join(in_string.rsplit(surname_ending, 1))
        lang_form = surname_lang_forms_in[surname_ending]['lang_form']
    return result, lang_form


def get_word_in_lang_form(in_string, in_lang_form):
    surname_ending = ''
    result = in_string
    if in_lang_form == 'I':
        result = in_string
    else:
        if in_string[-1:] in surname_lang_forms_out:
            surname_ending = in_string[-1:]
        elif in_string[-2:] in surname_lang_forms_out:
            surname_ending = in_string[-2:]
        if surname_ending != '':
            result = surname_lang_forms_out[surname_ending][in_lang_form].join(in_string.rsplit(surname_ending, 1))
    return result
