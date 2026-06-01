from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import ForeignKey
from engine import engine_postgresql


class Base(DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column
    rels_client = relationship('Order', back_populates='rels_order1')

    def __repr__(self):
        return f"Client(full name={self.full_name})"


class Goods(Base):
    __tablename__ = 'goods'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column
    status: Mapped[str] = mapped_column
    rels_goods = relationship('Order', back_populates='rels_order2')

    def __repr__(self):
        return (f"Goods: title= {self.name}\n"
                f"status= {self.status}")


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    list_goods: Mapped[str] = mapped_column
    quantity: Mapped[int] = mapped_column
    price: Mapped[float] = mapped_column
    sum_order: Mapped[float] = mapped_column
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))
    goods_id: Mapped[int] = mapped_column(ForeignKey('goods.id'))
    rels_order1 = relationship('Client', back_populates='rels_client')
    rels_order2 = relationship('Goods', back_populates='rels_goods')

    def __repr__(self):
        return (f"Order: list_goods= {self.list_goods}\n"
                f"quantity= {self.quantity}\n"
                f"price= {self.price}\n"
                f"sum_order= {self.sum_order}\n"
                f"client_id= {self.client_id}\n"
                f"goods_id= {self.goods_id}")


Base.metadata.create_all(engine_postgresql)



