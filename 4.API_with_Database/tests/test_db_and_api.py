import pytest
from API_with_Database.repo.json_ import post_object_json, update_object_json
from API_with_Database.models.store import Store
_id = 'ff8081818905fd0e018921968a89105f'


class TestApiAndDB:
    def test_post_and_insert(self, db_and_api):
        post = db_and_api.post_object(post_object_json)
        print(post)
        get_data = db_and_api.get_data_for_insert_and_update(post)
        db_and_api.insert_into_table(Store(id=get_data[0], product_name=get_data[1], creation_year=get_data[2],
                                           price=get_data[3], cpu_model=get_data[4], hard_disc_size=get_data[5]))
        select = db_and_api.select_specific_row('id', get_data[0])
        values = (get_data[0], 'Apple MacBook Pro 37', 2023, 1949.99, 'Intel Core i90', '2 TB')
        assert select[0] == values

    def test_put_and_update_price_by_id(self, db_and_api):
        put = db_and_api.update_object_api(_id, update_object_json)
        get_data = db_and_api.get_data_for_insert_and_update(put)
        db_and_api.update_price_by_id_db(get_data[0], get_data[3])
        select = db_and_api.select_specific_row('id', get_data[0])
        assert select[0][3] == get_data[3]

    @pytest.mark.parametrize('keyword, value', [('id', _id), ('name', 'Apple MacBook Pro 37'),
                                                ('data', {'year': 2023, 'price': 3949.99,
                                                          'CPU model': 'Intel Core i2019',
                                                          'Hard disk size': '2 TB', })])
    def test_update_cpu_model_by_year_db_and_put(self, db_and_api, keyword, value):
        db_and_api.update_cpu_model_by_year_db(2023, 'Intel Core i2019')
        select = db_and_api.select_specific_row('cpu_model', 'Intel Core i2019')
        get_cpu = select[0][4]
        put = db_and_api.update_api_object_in_sync_with_db(_id, 'Apple MacBook Pro 37', 2023, 3949.99, get_cpu, '2 TB')
        assert put[keyword] == value

    @pytest.mark.parametrize('keyword, value', [('id', _id), ('name', 'Apple MacBook Pro 37'),
                                                ('data', {'year': 2023, 'price': 4949.99,
                                                          'CPU model': 'Intel Core i2019',
                                                          'Hard disk size': '2 TB', })])
    def test_update_price_by_id_db_and_put(self, db_and_api, keyword, value):
        db_and_api.update_price_by_id_db(_id, 4949.99)
        select = db_and_api.select_specific_row('id', _id)
        get_price = select[0][3]
        put = db_and_api.update_api_object_in_sync_with_db(_id, 'Apple MacBook Pro 37', 2023, get_price,
                                                           'Intel Core i2019', '2 TB')
        assert put[keyword] == value

    @pytest.mark.parametrize('keyword, value', [('id', _id), ('name', 'Exclusive MacBook Pro'),
                                                ('data', {'year': 2023, 'price': 4949.99,
                                                          'CPU model': 'Intel Core i2019',
                                                          'Hard disk size': '2 TB', })])
    def test_update_product_name_db_and_put(self, db_and_api, keyword, value):
        db_and_api.update_product_name_db('Apple MacBook Pro 37', 'Exclusive MacBook Pro')
        select = db_and_api.select_specific_row('product_name', 'Exclusive MacBook Pro')
        get_name = select[0][1]
        put = db_and_api.update_api_object_in_sync_with_db(_id, get_name, 2023, 4949.99, 'Intel Core i2019', '2 TB')
        assert put[keyword] == value


