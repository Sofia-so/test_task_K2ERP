from app import session
from db import Goods, Client


def filling_goods():
    goods_list = [
        Goods(name="Товар1", price=456.8, status="В наявності"),
        Goods(name="Товар2", price=476, status="В наявності"),
        Goods(name="Товар3", price=17723.6, status="Немає в наявності"),
        Goods(name="Товар4", price=47, status="В наявності"),
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
    filling_goods()
    create_client()