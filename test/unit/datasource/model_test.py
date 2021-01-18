import unittest
from mock import Mock


from datasource.model import IQDataSource


class TestIQDataSource(unittest.TestCase):

    def test_get_list_of_table_names_works(self):
        mock_iq_gateway = Mock()
        my_iq_ds = IQDataSource(name='Тестовый источник', gateway=mock_iq_gateway)
        data = ['d_entity', 'd_currency', 'd_account']
        mock_iq_gateway.get_list_of_table_names.return_value = data
        self.assertListEqual(
            list1=['d_entity', 'd_currency', 'd_account'],
            list2=my_iq_ds.get_list_of_table_names())


if __name__ == '__main__':
    unittest.main()
