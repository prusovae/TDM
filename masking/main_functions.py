import csv
import os

profiling_result_domains = dict()


def load_profiling_results(jira_task):
    profiling_results_path = os.path.join('4devonly', 'shared_folder', jira_task, 'profiling_results.csv')
    # считываем результаты профилирования таблиц в справочник
    # ключом будет имя таблицы+";"+имя колонки а значением справочника будет бизнес домен

    with open(profiling_results_path, newline='', encoding='utf-8') as file:
        data = csv.reader(file, delimiter=',')
        # skip header
        next(data)
        for table_name, column_name, domain_name, pct in data:
            if table_name not in profiling_result_domains:
                profiling_result_domains[table_name] = dict()
                profiling_result_domains[table_name][column_name] = domain_name
            else:
                profiling_result_domains[table_name][column_name] = domain_name


def get_column_domain(table_name, column_name):
    # Отрезаем расширение, в случае если передаваемое имя - имя файла, например, customers.csv
    table_name = os.path.splitext(table_name)[0]
    profiling_result_table_columns = dict()
    profiling_result_domain = ''
    if table_name in profiling_result_domains:
        profiling_result_table_columns = profiling_result_domains.get(table_name)
        if column_name in profiling_result_table_columns:
            profiling_result_domain = profiling_result_table_columns.get(column_name)
    return profiling_result_domain
