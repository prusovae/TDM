import os
import json

from datasource.model import DataSource, OracleDataSource, IQDataSource, CSVDataSource
from datasource.gateway import IQGateway


def get_datasource_config(jira_task):
    config_file_path = os.path.join('4devonly', 'shared_folder', jira_task, 'config.json')
    with open(config_file_path, encoding='utf-8') as json_file:
        config_data = json.load(json_file)
        json_property = dict(config_data)
    return json_property


def get_datasources(task_id: str) -> (DataSource, DataSource):
    """Возвращает два объекта DataSource источника и DataSource приемника"""
    conf = get_datasource_config(jira_task=task_id)
    datasource_from = None
    datasource_to = None

    if conf['data_source_type'] == 'oracle':
        datasource_from = OracleDataSource(
            name=conf['data_source_name'], host=conf['data_source_host'], port=conf['data_source_port'],
            sid=conf['data_source_sid'], user=conf['data_source_user'], password=conf['data_source_password'],
            table_owner=conf['data_source_table_owner']
        )
    elif conf['data_source_type'] == 'iq':
        gateway_from = IQGateway(
            host=conf['data_source_host'], port=conf['data_source_port'], dbname=conf['data_source_dbname'],
            username=conf['data_source_username'], password=conf['data_source_password'])
        datasource_from = IQDataSource(name=conf['data_source_name'], gateway=gateway_from)
    elif conf['data_source_type'] == 'csv':
        csv_data_source_folder = os.path.join('4devonly', 'shared_folder', task_id, 'source')
        datasource_from = CSVDataSource(path=csv_data_source_folder)
    else:
        # TODO: вернуть исключение что не удалось определить систему источник
        pass

    if conf['data_target_type'] == 'oracle':
        datasource_to = OracleDataSource(
            name=conf['data_target_name'], host=conf['data_target_host'], port=conf['data_target_port'],
            sid=conf['data_target_sid'], user=conf['data_target_user'], password=conf['data_target_password'],
            table_owner=conf['data_target_table_owner']
        )
    elif conf['data_target_type'] == 'iq':
        gateway_to = IQGateway(
            host=conf['data_target_host'], port=conf['data_target_port'], dbname=conf['data_target_dbname'],
            username=conf['data_target_username'], password=conf['data_target_password'])
        datasource_to = IQDataSource(name=conf['data_target_name'], gateway=gateway_to)
    elif conf['data_target_type'] == 'csv':
        csv_data_target_folder = os.path.join('4devonly', 'shared_folder', task_id, 'target')
        datasource_to = CSVDataSource(path=csv_data_target_folder)
    return datasource_from, datasource_to
