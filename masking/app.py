import time

from masking.main_functions import load_profiling_results, get_column_domain
from masking.masking_functions import domain_func_mapping, load_datamasking_dicts
from datasource.controller import get_datasources

# замер времени работы скрипта
start_time = time.process_time()
# TODO: добавить парсинг агрументов командной строки и вынести туда JIRA-NUM
#   продумать API приложения, какие аргументы и команды должны быть в принципе, например:
#   - получить список всех JIRA-задач
#   - получить статистику по отдельной JIRA-задаче (кол-во таблиц/колонок всего и для которых нужна обезличка)
#   - запустить обезличку для конкретной JIRA-задачи
globalTask = "JIRA004"
# Загружаем в память все необходимые справочники для обезлички
start_time_save_table = time.process_time()
load_datamasking_dicts()
print('load_datamasking_dicts '"{:g} s".format(time.process_time() - start_time_save_table))
# считываем результаты профилирования таблиц в справочник
load_profiling_results(globalTask)


######################################     Основной код    ########################################
if __name__ == '__main__':
    # А так можно получить все таблицы из источника:
    # tables = [datasource.get_table(table_name) for table_name in datasource.get_list_of_tables()]
    
    # src, tgt = get_datasources(globalTask)
    # tables = src.get_list_of_table_names()
    # # Для каждой таблицы выполняем одинаковый код обезлички
    # for table_name in tables:
    #     df = src.get_table(table_name)
    #     # Загружаем частями по 100 тыс. записей из таблицы на тот случай если она огромная
    #     # todo-high-prusove: решить что делать с chunk-ами, т.к. в iq пока это не будет работать
    #     for chunk in df:
    #         # Для каждой колонки проверяем её домен из файла profiling_results.csv
    #         for column in chunk.columns:
    #             column_name = column.__str__()
    #             data_masking_domain = get_column_domain(table_name, column_name)
    #             if domain_func_mapping.get(data_masking_domain) is not None:
    #                 # Для каждого домена отработает своя функция
    #                 chunk[column] = chunk[column].map(lambda x: domain_func_mapping[data_masking_domain]())
    #         # Сохраняем результат
    #         tgt.save_table('masked_'+table_name, chunk)

    src, tgt = get_datasources(globalTask)
    tables = src.get_list_of_table_names()
    # Для каждой таблицы выполняем одинаковый код обезлички
#     for table_name in tables:
#         print(f'Формирование df из таблицы {table_name} запущено ')
#         df = src.get_table(table_name)
#         print(f'Формирование df из таблицы {table_name} завершено ')
#         # Загружаем частями по 100 тыс. записей из таблицы на тот случай если она огромная
#         # todo-high-prusove: решить что делать с chunk-ами, т.к. в iq пока это не будет работать
#         for column in df.columns:
#
#             column_name = column.__str__()
#             data_masking_domain = get_column_domain(table_name, column_name)
#             if domain_func_mapping.get(data_masking_domain) is not None:
#                 # Для каждого домена отработает своя функция
#                 df[column] = df[column].map(lambda x: domain_func_mapping[data_masking_domain]())
#                 print('обработка по колонкам '"{:g} s".format(time.process_time() - start_time_save_table), data_masking_domain)
#         # Сохраняем результат
#
#         print('до вызова save_table '"{:g} s".format(time.process_time() - start_time_save_table))
#         tgt.save_table(table_name, df)
#         #tgt.save_table_odbc(table_name, df)
#         print('после вызова save_table '"{:g} s".format(time.process_time() - start_time_save_table))
#     # замер времени работы скрипта
# print ('Общее время работы скрипта обезличивания = '"{:g} s".format(time.process_time() - start_time_save_table))
    for table_name in tables:
        print(f'Формирование df из таблицы {table_name} запущено ')
        df = src.get_table(table_name)
        k=0
        for chunk in df:
            k+=1
            print('chunk #',k)
            if chunk is not None:

                # Загружаем частями по 100 тыс. записей из таблицы на тот случай если она огромная
                # todo-high-prusove: решить что делать с chunk-ами, т.к. в iq пока это не будет работать
                for column in chunk.columns:

                   column_name = column.__str__()
                   data_masking_domain = get_column_domain(table_name, column_name)
                   if domain_func_mapping.get(data_masking_domain) is not None:
                        #Для каждого домена отработает своя функция
                       chunk[column] = chunk[column].map(lambda x: domain_func_mapping[data_masking_domain]())
                       #print('обработка по колонкам '"{:g} s".format(time.process_time() - start_time_save_table), data_masking_domain)
                #Сохраняем результат

                #print('до вызова save_table '"{:g} s".format(time.process_time() - start_time_save_table))
                tgt.save_table(table_name, chunk)
                #tgt.save_table_odbc(table_name, df)
                #print('после вызова save_table '"{:g} s".format(time.process_time() - start_time_save_table))
        # замер времени работы скрипта
print ('Общее время работы скрипта обезличивания = '"{:g} s".format(time.process_time() - start_time_save_table))