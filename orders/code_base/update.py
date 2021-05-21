from . import get

def update_order_paid(order_id):
    try:
        order = get.get_order_by_id(order_id, raw=True)
        if (order is None):
            raise Exception()
        order.is_paid = True
        order.save()

        return True
    except:
        return False