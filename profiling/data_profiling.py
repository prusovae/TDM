#Всё что снизу это пока куча мусора

import os
import pandas as pd
import json
from sklearn.model_selection import train_test_split#, GridSearchCV

def prepare_data(df):
    #переводим текст в lower формат, удаляем пробелы слева, справа и удаляем все множественные пробелы
    df['txt']=df['txt'].str.lower().str.strip().str.replace(' +', ' ')
    #df['txt']=df['txt'].str.lower()
    df['len']=df.txt.str.len()
    #df['digits_len'] = df.txt.map(lambda x: len([k for k in x if k.isdigit()]))
    df['digits_len'] = df.txt.str.count('[0-9]')
    #df['alpha_len'] = df.txt.map(lambda x: len([k for k in x if k.isalpha()]))
    df['alpha_len'] = df.txt.str.count('[A-Za-zА-Яа-яЁё]')
    df['dot_len']=df.txt.str.count('\.')
    df['space_len']=df.txt.str.count(' ')
    df['dash_len']=df.txt.str.count('\-')
    df['plus_len']=df.txt.str.count('\+')
    df['comma_len']=df.txt.str.count(',')
    df['bracket']=df.txt.str.count('[()]')
    df['midname_ending'] = 0
    df.loc[df['txt'].str[-3:].isin(['вич','вна']) , 'midname_ending'] = 1
    df['name_ending'] = 0
    df.loc[df['txt'].str[-2:].isin(['ов','ев']) , 'name_ending'] = 1
    df.loc[df['txt'].str[-3:].isin(['ова','ева']) , 'name_ending'] = 1
    #df = df.drop(['txt'], axis=1)
    return df

domains_path = os.path.join('data','domains')
data_path = os.path.join('z:')
lang_forms_path = os.path.join('data','lang_forms')
df = pd.read_csv(os.path.join(data_path, 'test.csv'), encoding='utf-8')
df_test = prepare_data(df)
check_if_column_is_complex = df_test['space_len'].mean()
if check_if_column_is_complex > 2:
    pass


#surname_lang_forms.json


with open(os.path.join(lang_forms_path, 'surname_lang_forms_in.json'), encoding='utf-8') as json_file:
    my_json = dict(json.load(json_file))