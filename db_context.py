from app import session
from db import Goods, Client


def filling_goods():
    goods_list = [
        Goods(name="Товар1", status="В наявності"),
        Goods(name="Товар2", status="В наявності"),
        Goods(name="Товар3", status="Немає в наявності"),
        Goods(name="Товар4", status="В наявності"),
    ]

    session.add_all(goods_list)
    session.commit()


def create_client():
    clients = [
    Client(full_name="Firstnam Las"),
    Client(full_name="Firstn Las")
    ]
    session.add_all(clients)
    session.commit()


if __name__ == "__main__":
    create_client()