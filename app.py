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


@app.route('/order_client')
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


@app.route('/goods')
def goods():
    goods_list = session.query(Goods).all()
    return render_template(
        'items.html',
        goods_list=goods_list
    )


@app.route('/goods', methods=['POST'])
def add_goods():
    name = request.form.get('name')
    status = request.form.get('status')
    new_goods = Goods(
        name=name,
        status=status
    )

    session.add(new_goods)
    session.commit()

    return redirect('/')


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
    price = float(request.form["price"])
    sum_order = quantity * price
    order = Order(
        list_goods=list_goods,
        quantity=quantity,
        price=price,
        sum_order=sum_order
    )

    session.add(order)
    session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)



