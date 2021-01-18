import os
import time
import numpy as np


from masking.lingvo_functions import load_lang_forms
from masking.masking_functions import load_datamasking_dicts
from profiling.profiling_functions import define_domain
from datasource.controller import get_datasources

# замер времени работы скрипта
start_time = time.process_time()
# todo-low-prusove: вынести номер задачи в аргументы программы и переименовать на task_id
globalTask = "JIRA005"
profiling_results_path = os.path.join('4devonly', 'shared_folder', globalTask, 'profiling_results.csv')
# Загружаем в память все необходимые справочники для обезлички
load_datamasking_dicts()
load_lang_forms()


######################################     Основной код    ########################################
if __name__ == '__main__':
    src, tgt = get_datasources(globalTask)
    tables = src.get_list_of_table_names()
    result_profiling_list = ['table_name,column_name,data_masking_domain,pct']
    # Для каждой таблицы выполняем одинаковый код обезлички
    for table_name in tables:
        # временно берем всю таблицу, нужно заменить на get1000notnullrows в будущем
        df = src.get1000notnullrows(table_name)
        print(df)
        for column in df.columns:
            # todo-medium-asyunov нужно еще удалять все знаки препинания, заменять их на пробелы
            # удаляем все множественные пробелы
            df[column] = df[column].astype(np.str).str.replace(' +', ' ')
            df[column] = df[column].str.lower().str.strip()
            data_masking_domain, pct = define_domain(df[column])
            if data_masking_domain != '':
                # Отрезаем расширение, в случае если передаваемое имя - имя файла, например, customers.csv
                table_name = os.path.splitext(table_name)[0]
                result_profiling_list.append(table_name + ',' + column + ',' + data_masking_domain + ',' + str(pct))

    # Сохраняем результат
    with open(profiling_results_path, 'w') as f:
        for item in result_profiling_list:
            # todo-low-prusove: переписать на f-стринг
            f.write("%s\n" % item)

    # замер времени работы скрипта
    print('Общее время работы скрипта профилирования = '"{:g} s".format(time.process_time() - start_time))
