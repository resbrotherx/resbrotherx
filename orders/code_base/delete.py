from orders.models import Order
from . import get

def delete_order_by_item_id(item_id, user_id):
    try:
        order = get.get_order_by_item_id(item_id=item_id,user_id=user_id, raw=True)
        if order is None:
            raise Exception("No order record found")
        order.delete()
        order = True
    except Exception as ex:
        print(str(ex))
        order = False
    return order


def delete_order_by_id(order_id):
    try:
        order = get.get_order_by_id(order_id=order_id, raw=True)
        if order is None:
            raise Exception("No order record found")
        order.delete()
        order = True
    except Exception as ex:
        print(str(ex))
        order = False
    return order