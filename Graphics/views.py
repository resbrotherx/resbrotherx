from django.shortcuts import render
from .models import Graphics
from django.shortcuts import render, get_object_or_404
from .models import Category as categor
from django.db.models import Q

def graphics(request):
    graphic = Graphics.objects.all()
    cat_all = categor.objects.all()
    context={
        'graphic':graphic,
        "cat":cat_all,
    }
    return render(request, 'graphic/graphic.html', context)

# def art_prints(request):
#     # print = Prints.objects.all()

#     # context={
#     #     'print':print
#     # }
#     return render(request, 'art_prints.html')
    
def graphics_category(request, slug):
    categories = categor.objects.all()
    graphic = Graphics.objects.all()
    if slug:
        category = get_object_or_404(categor, slug=slug)
        graphic = graphic.filter(category=category)
    template = "graphic/graphics_category.html"
    context = {
        'categories': categories,
        'graphic': graphic,
        'category': category,
    }
    return render(request, template, context)


def search(request):
    item = Graphics.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = item.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context={
        'queryset':queryset
    }
    return render(request, 'graphic/search-page.html', context)


    

def graphic_details(request, id):
    post_all = Graphics.objects.all()
    graphic = get_object_or_404(Graphics, id=id)
    categories = categor.objects.all()
    # PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        "graphic":graphic,
        'post_all':post_all,
        'categories': categories,
        # 'trend':trend,
    }
    return render(request,'graphic/graphic_details.html', context)

