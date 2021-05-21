from django.urls import path
from django.urls.conf import include
from . import views
from items import views as item_view
from orders import views as order_view
from django.views.decorators.csrf import csrf_exempt

app_name = 'api'

items = [
    path('all/', item_view.get_all_items),
    path('max-min/', item_view.get_max_min_prices),
    path('filter/', csrf_exempt(item_view.filter_items)), 
]

orders = [
    path('create/', csrf_exempt(order_view.create_order)),
    path('delete/', csrf_exempt(order_view.delete_order)),
    path('paid/', csrf_exempt(order_view.mark_order_as_paid)),
    
]

apipatterns = [
    path('items/', include(items)),
    path('orders/', include(orders)),
]


urlpatterns = [
    path('v1/', include(apipatterns)),
]