from flask import (
    Flask,
    request,
    jsonify,
    redirect,
    render_template
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from engine import engine_postgresql
from db import (
    Client,
    Goods,
    Order
)
from schemas import (client_schema)

app = Flask(__name__)

Session = sessionmaker(bind=engine_postgresql)
session = Session()


@app.route('/client')
def client():
    return render_template('client.html')


@app.route('/order_client', methods=['GET'])
def order_client():
    orders = session.scalars(
        select(Order).where(Order.client_id == client.id)
    ).all()
    client_orders = orders
    return render_template(
        'order_client.html',
        client_orders=client_orders
    )


@app.route('/client', methods=['POST'])
def add_client():
    data = request.json
    new_client = Client(full_name=data['full_name'])
    session.add(new_client)
    session.commit()

    return jsonify(
        client_schema.dump(new_client)
), 201


@app.route('/goods', methods=['GET'])
def goods():
    goods_list = session.scalars(select(Goods)).all()
    return render_template(
        'items.html',
        goods_list=goods_list
    )


@app.route('/goods_add', methods=['POST'])
def add_goods():
    name = request.form.get('name')
    status = request.form.get('status')
    price = request.form.get('price')
    new_goods = Goods(
        name=name,
        price=price,
        status=status
    )

    session.add(new_goods)
    session.commit()

    return redirect('/goods')


@app.route("/")
def index():
    return render_template("template.html")


@app.route("/orders")
def order():
    todo_list = session.query(Order).all()
    return render_template(
        "order.html",
        todo_list=todo_list
    )


@app.route("/order", methods=["POST"])
def create_order():
    list_goods = request.form.get('list_goods')
    quantity = int(request.form["quantity"])
    client_id = request.form.get('client_id')
    goods_id = session.scalar(
        select(Goods.id).where(Goods.name == list_goods)
    )
    product_price = session.scalar(
        select(Goods.price).where(Goods.name == list_goods)
    )
    sum_order = quantity * product_price
    order = Order(
        list_goods=list_goods,
        quantity=quantity,
        client_id=client_id,
        goods_id=goods_id,
        sum_order=sum_order
    )

    try:
        session.add(order)
        session.commit()

    except Exception as e:
        session.rollback()
        print(e)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
