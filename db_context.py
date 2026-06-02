from app import session
from db import Goods
from engine import engine_postgresql


def filling_goods():
    goods_list = [
        Goods(name="Товар1", status="В наявності"),
        Goods(name="Товар2", status="В наявності"),
        Goods(name="Товар3", status="Немає в наявності"),
        Goods(name="Товар4", status="В наявності"),
    ]

    session.add_all(goods_list)
    session.commit()

