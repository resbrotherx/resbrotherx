from django.shortcuts import render
from .code_base import create, get, delete, update
from django.http import JsonResponse

def prepare_json(code, data, passed_message=None):
    message = "Action Successful"
    # if code = 1: create/update action occurred, 0:read action occured, -1:create/update failed, -2
    if code < 0:
        message = "An error occured."
    if code == -2:
        message = "A system error has occurred."
    if passed_message:
        message = passed_message
    status = True
    if code < 0:
        status = False
    return JsonResponse({
        "status": status,
        "code": code,
        "data": data,
        "message": message
    })

# Create your views here.
def create_order(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        # incase form doesnt need ajax
        if request.method == "POST":
            res = create.create_order(request.POST['user_id'],request.POST['item_id'])
            if "exception" in res and res["exception"]:
                return prepare_json(-2, {}, res["message"])
            return prepare_json(res["status"], res["order"])
        else:
            return prepare_json(-1, {}, "Request mode incorrect.")

def get_order(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        # incase form doesnt need ajax
        order  = get.get_order_by_item_id(request.POST["item_id"], request.POST["user_id"])
        if order is not None:
            return (prepare_json(0, order))
        else:
            return (prepare_json(-1, {}, res["message"]))

def delete_order(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        # incase form doesnt need ajax
        if 'item_id' in request.POST:
            res  = delete.delete_order_by_item_id(request.POST["item_id"], request.POST["user_id"])
        elif 'order_id' in request.POST:
            res  = delete.delete_order_by_id(request.POST["order_id"])
        if not res:
            return (prepare_json(-1, {}, "No order record found"))
        return (prepare_json(1, {}))

def mark_order_as_paid(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        # incase form doesnt need ajax
        res = update.update_order_paid(request.POST['order_id'])
        if not res:
            return (prepare_json(-1, {}, "No order record found"))
        return (prepare_json(1, {}))
            