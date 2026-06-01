from marshmallow import(
    Schema,
    fields,
    validate
)

class ClientSchema(Schema):
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True)


class GoodsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    list_goods = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=validate.Length(min=1))
    price = fields.Float()
    sum_order = fields.Float()
    client_id =  fields.Int()
    goods_id =  fields.Int()


client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)
goods_schema = GoodsSchema()
goodses_schema = GoodsSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)