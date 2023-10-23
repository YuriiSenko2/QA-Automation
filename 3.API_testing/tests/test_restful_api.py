import pytest
from API_testing.json_for_posts_and_updates import post_object_json, patch_object_json, update_object_json
object_id = 'ff8081818905fd0e01892046af560fe8'


class TestInformationReception:
    def test_get_all_original_objects_status_code(self, get):
        status = get.get_all_original_objects()
        assert status[0] == 200

    def test_number_of_original_objects(self, get):
        body = get.get_all_original_objects()
        number = len(['id' for el in body[1]])
        assert number == 13

    @pytest.mark.parametrize('keyword, value', [('id', '3'), ('name', 'Apple iPhone 12 Pro Max'),
                                            ('data', {'capacity GB': 512, 'color': 'Cloudy White'})])
    def test_get_single_object(self, get, keyword, value):
        objects = get.get_single_object(3)
        assert objects[1][keyword] == value

    def test_get_single_object_status_code(self, get):
        status_code = get.get_single_object(3)
        assert status_code[0] == 200

    @pytest.mark.parametrize('keyword, value', [('id', '3'), ('name', 'Apple iPhone 12 Pro Max'),
                                            ('data', {'capacity GB': 512, 'color': 'Cloudy White'})])
    @pytest.mark.parametrize('keyword1, value1', [('id', '5'), ('name', 'Samsung Galaxy Z Fold2'),
                                              ('data', {'color': 'Brown', 'price': 689.99})])
    def test_get_multiple_objects(self, get, keyword, value, keyword1, value1):
        objects = get.get_multiple_objects('id=3&id=5')
        assert objects[0][keyword] == value and objects[1][keyword1] == value1


class TestChangeAndAdditionOfInformation:
    @pytest.mark.parametrize('keyword, value', [('name', 'Apple MacBook Pro 26'),
                                                ('data', {'year': 2018, 'price': 1849.99, 'CPU model': 'Intel Core i9',
                                                          'Hard disk size': '1 TB'})])
    def test_post_request(self, modifications, keyword, value):
        post_req = modifications.post_object(post_object_json)
        retrieve_id = modifications.get_particular_value(post_req, 1, 'id')
        assert post_req[1][keyword] == value and post_req[0] == 200
        print(retrieve_id)

    @pytest.mark.parametrize('keyword, value', [('id', object_id), ('name', 'Apple MacBook Pro 27'),
                                                ('data', {'year': 2022, 'price': 3949.99, 'CPU model': 'Intel Core i9',
                                                          'Hard disk size': '1 TB', 'Availability': 'No'})])
    def test_put_request(self, modifications, keyword, value):
        put_req = modifications.update_object(object_id, update_object_json)
        assert put_req[1][keyword] == value and put_req[0] == 200

    @pytest.mark.parametrize('keyword, value', [('name', 'Apple MacBook SuperPro 2023')])
    def test_patch_request(self, modifications, keyword, value):
        patch_req = modifications.update_object(object_id, patch_object_json)
        assert patch_req[1][keyword] == value and patch_req[0] == 200

    @pytest.mark.parametrize('keyword, value', [('message', f'Object with id = {object_id} has been deleted.')])
    def test_delete_request(self, modifications, keyword, value):
        del_req = modifications.delete_object(object_id)
        assert del_req[1][keyword] == value and del_req[0] == 200

