import requests
from API_testing.api_config import config
import json


class GetRequests:
    def __init__(self):
        self.common_url = f"{config['host']}"
        self.header = {
            "content-type": "application/json"
        }

    def get_all_original_objects(self):
        response = requests.get(self.common_url, headers=self.header)
        return response.status_code, response.json()

    def get_single_object(self, identifications):
        single_object = requests.get(f"{self.common_url}/{identifications}", headers=self.header)
        return single_object.status_code, single_object.json()

    def get_multiple_objects(self, identifications):
        objects = requests.get(f"{self.common_url}?{identifications}")
        return objects.json()

    def get_particular_value(self, response, key_number, key_value):
        dump = json.dumps(response)
        loads = json.loads(dump)
        return loads[key_number][key_value]


class PostPutPatchDeleteRequests(GetRequests):
    def __init__(self):
        super().__init__()

    def post_object(self, object_data):
        create_object = requests.post(self.common_url, data=object_data, headers=self.header)
        return create_object.status_code, create_object.json()

    def update_object(self, identification, updates):
        update = requests.put(f"{self.common_url}/{identification}", data=updates, headers=self.header)
        return update.status_code, update.json()

    def partially_update_object(self, identification, partial_update):
        partial_modification = requests.patch(f"{self.common_url}/{identification}", data=partial_update,
                                              headers=self.header)
        return partial_modification.status_code, partial_modification.json()

    def delete_object(self, identification):
        deletion = requests.delete(f"{self.common_url}/{identification}", headers=self.header)
        return deletion.status_code, deletion.json()



