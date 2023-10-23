from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Integer, Column

Base = declarative_base()


class Store(Base):
    __tablename__ = 'store_info'
    id = Column(VARCHAR(50), primary_key=True)
    product_name = Column(VARCHAR(50))
    creation_year = Column(Integer)
    price = Column(Integer)
    cpu_model = Column(VARCHAR(50))
    hard_disc_size = Column(VARCHAR(50))

    def __str__(self):
        return f"[id = {self.id}, product_name = {self.product_name}, creation_year = {self.creation_year}, " \
               f"price = {self.price}, cpu_model = {self.cpu_model}, hard_disc_size = {self.hard_disc_size}]"