from API_with_Database.session import session
from API_with_Database.models.store import Store
import requests
import json
from API_with_Database.repo.api_config import config
from sqlalchemy import update, text


class StoreRepo:
    def __init__(self):
        self.__session = session
        self.common_url = f"{config['host']}"
        self.header = {
            "content-type": "application/json"
        }

    def post_object(self, object_data):
        create_object = requests.post(self.common_url, data=object_data, headers=self.header)
        return create_object.json()

    def update_object_api(self, identification, updates):
        update_ = requests.put(f"{self.common_url}/{identification}", data=updates, headers=self.header)
        return update_.json()

    def update_api_object_in_sync_with_db(self, id_, name, year, price, cpu, hard_disc):
        update_object = json.dumps({
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": cpu,
                "Hard disk size": hard_disc,
            }
        })
        _update = requests.put(f"{self.common_url}/{id_}", data=update_object, headers=self.header)
        return _update.json()

    def get_data_for_insert_and_update(self, response):
        result = list(response.values())[0:2]
        for el in response['data'].values():
            result.append(el)
        return result

    def insert_into_table(self, values: Store):
        self.__session.add(values)
        self.__session.commit()

    def select_specific_row(self, column_, value_):
        sql = text(f"SELECT * from store_info where {column_} = '{value_}'")
        result = self.__session.execute(sql).fetchall()
        return result

    def get_all(self):
        for product in self.__session.query(Store).all():
            print(product)

    def update_price_by_id_db(self, id_, new_price):
        stmt = (
            update(Store)
            .where(Store.id == str(id_))
            .values(price=new_price)
            .execution_options(synchronize_session=False)
        )
        self.__session.execute(stmt)
        self.__session.commit()

    def update_cpu_model_by_year_db(self, year_, cpu):
        stmt = (
            update(Store)
            .where(Store.creation_year == str(year_))
            .values(cpu_model=cpu)
            .execution_options(synchronize_session=False)
        )
        self.__session.execute(stmt)
        self.__session.commit()

    def update_product_name_db(self, old_name, new_name):
        stmt = (
            update(Store)
            .where(Store.product_name == str(old_name))
            .values(product_name=new_name)
            .execution_options(synchronize_session=False)
        )
        self.__session.execute(stmt)
        self.__session.commit()




