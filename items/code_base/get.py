from items.models import Item
from django.db.models import Q, Max, Min
from django.shortcuts import get_list_or_404

limit = 3

def get_all_items(page=1):
    content_limit = limit * page
    try:
        items = get_list_or_404(Item, Q(id__lte=(content_limit)))[(content_limit - limit):content_limit]
        items_temp = items
        items = []
        for item in items_temp:
            items.append(get_item(item))
    except:
        items = []
    return items

def get_max_min_prices():
    max_item = Item.objects.aggregate(Max('price'))
    min_item = Item.objects.aggregate(Min('price'))
    return {
        "max_price": max_item['price__max'],
        "min_price": min_item['price__min'],
    }

def get_item_by_filter(min, max):
    try:
        # 
        items_temp = Item.objects.filter(Q(price__range=(min, max)))
        items = []
        for item in items_temp:
            items.append(get_item(item))
    except:
        items = []
    return items

def get_item_by_id(id):
    try:
        item = Item.objects.get(id=(id))
        item = get_item(item)
    except:
        item = None
    return item


def get_item(item):
    return {
        "id": item.id,
        "title": item.title,
        "created_on": item.created_on.strftime("%d-%m-%Y, %H:%M:%S"),
        "item_created_date": item.item_created_date.strftime("%d-%m-%Y, %H:%M:%S"),
        "user": {
            "name": item.user.first_name + " " + item.user.last_name,
            "first_name": item.user.first_name,
            "last_name": item.user.last_name,
            "phone": item.user.phone_number,
            "gender": item.user.gender,
        },
        "item_type": item.item_type,
        "price": item.price,
        "image": item.image,
        "image_path": item.image_path,

    }

