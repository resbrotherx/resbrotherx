from orders.models import Order
from user.models import User
from items.models import Item
from django.db.models import Q, Max, Min
from django.shortcuts import get_list_or_404
from . import get

def create_order(user_id, item_id):
    try:
        status = 1
        
        item = Item.objects.get(pk=item_id)
        order = Order.objects.filter(user=user_id, item=item, price=item.price, status="0")
        if not order:
            order = Order(user=User.objects.get(pk=user_id), item=item, price=item.price)
            order.save()
        else:
            order = order[0]
            status = 2
        order_detail = get.order_detail(order)
        order_detail["donwload_link"] = item.image_path + item.image
        order_detail["filename"] = item.image
        return {"status": status, "order": order_detail}
    except Exception as ex:
        return {"exception": True, "message": str(ex)}