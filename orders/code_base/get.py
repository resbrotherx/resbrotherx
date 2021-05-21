from orders.models import Order

def order_detail(order):
    return {
        "id": order.id,
        "price": order.price,
        "status": order.status,
        "status_display": order.get_status_display(),
        "created_on": order.created_on,
        "finalized_on": order.finalized_on,
        "user": {
            "name": order.user.first_name + " " + order.user.last_name,
            "first_name": order.user.first_name,
            "last_name": order.user.last_name,
            "phone": order.user.phone_number,
            "gender": order.user.gender,
        },
    }

def get_order_by_item_id(item_id, user_id, raw=False):
    try:
        # 
        order = Order.objects.filter(item__id=item_id, user__id=user_id)[0]
        if not raw:
            order = order_detail(order)
    except:
        order = None
    return order


def get_order_by_id(order_id, raw=False):
    try:
        # 
        order = Order.objects.filter(id=order_id)[0]
        if not raw:
            order = order_detail(order)
    except:
        order = None
    return order