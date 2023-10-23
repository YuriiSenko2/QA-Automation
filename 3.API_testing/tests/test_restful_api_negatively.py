import requests
from API_testing.api_config import config, wrong_config
from API_testing.json_for_posts_and_updates import post_object_json, update_object_json, wrong_patch_object_json
from API_testing.headers import header, wrong_header
from API_testing.object_for_negative_testing import identification
wrong_id = 'fewgsg43t435523532twgtewgsdvdsbfsh'


class TestNegatively:
    def test_get_with_wrong_config(self):
        try:
            response = requests.get(f"{wrong_config['host']}")
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            assert error.response.status_code == 404

    def test_post_with_wrong_header(self):
        try:
            create_object = requests.post(f"{config['host']}", data=post_object_json, headers=wrong_header)
            create_object.raise_for_status()
        except requests.exceptions.HTTPError as error:
            assert error.response.status_code == 415

    def test_put_with_wrong_id(self):
        try:
            update_object = requests.put(f"{config['host']}/{wrong_id}", data=update_object_json, headers=header)
            update_object.raise_for_status()
        except requests.exceptions.HTTPError as error:
            assert error.response.status_code == 404

    def test_patch_with_wrong_json(self):
        try:
            patch_object = requests.patch(f"{config['host']}/{identification}", data=wrong_patch_object_json,
                                          headers=header)
            patch_object.raise_for_status()
        except requests.exceptions.HTTPError as error:
            assert error.response.status_code == 404

    def test_delete_deleted_object(self):
        requests.delete(f"{config['host']}/{identification}", headers=header)
        try:
            delete_deleted_object = requests.delete(f"{config['host']}/{identification}", headers=header)
            delete_deleted_object.raise_for_status()
        except requests.exceptions.HTTPError as error:
            assert error.response.status_code == 404

