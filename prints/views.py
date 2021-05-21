from django.shortcuts import render
from .models import Prints
from django.shortcuts import render, get_object_or_404
from .models import Category as categor

def prints(request):
    print = Prints.objects.all()
    cat_all = categor.objects.all()
    context={
        'print':print,
        "cat":cat_all,
    }
    return render(request, 'prints.html', context)

# def art_prints(request):
#     # print = Prints.objects.all()

#     # context={
#     #     'print':print
#     # }
#     return render(request, 'art_prints.html')
    
def art_category(request, slug):
    categories = categor.objects.all()
    post = Prints.objects.all()
    if slug:
        category = get_object_or_404(categor, slug=slug)
        post = post.filter(category=category)
    template = "artcategory.html"
    context = {
        'categories': categories,
        'post': post,
        'category': category,
    }
    return render(request, template, context)



def print_details(request, id):
    post_all = Prints.objects.all()
    prints = get_object_or_404(Prints, id=id)
    categories = categor.objects.all()
    # PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        "prints":prints,
        'post_all':post_all,
        'categories': categories,
        # 'trend':trend,
    }
    return render(request,'print_details.html', context)

