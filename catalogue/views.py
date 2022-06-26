from django.contrib.auth.decorators import login_required
from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import classonlymethod
from django.views.generic import View

from catalogue.models import Category, CategoryProduct, Product


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class CatalogueView(View):
    clpages = 0
    @classonlymethod
    def index(cls, request, category = None):
        cls.clpages = 0
        products = None

        if category:
        # """
        # ? Выбираю категорию по имени
        # ? Фильтрую продукты которые соответствуют категории(id)
        # ? Выбираю только поле с id продуктов
        # ? Фильтрую продукты(получаю уже сами продукты)
        # """
            products = list(Product.objects.filter(id__in=CategoryProduct.objects.filter(category=Category.objects.get(title=category)).values('product')).values())
        else:
            products = list(Product.objects.all().values())
        context = {
            "title": "Barsik Shop",
            "logedin": request.user.is_authenticated,
            "left_menu": Category.objects.order_by("title").all(),
            "selected_category": category,
            "products": products,
            "basket_items": request.session.get('basket', None),
        }
        return render(request, 'catalogue/catalogue.html', context)

    """
    * Загружает контент с базы данных на страницу
    """
    @classonlymethod
    def loadview(cls, request, category=None):
        if is_ajax(request):
            x = int(request.GET.get('value', 0))
            category = request.GET.get('category', None)
            if category:
            # """
            # ? Выбираю категорию по имени
            # ? Фильтрую продукты которые соответствуют категории(id)
            # ? Выбираю только поле с id продуктов
            # ? Фильтрую продукты(получаю уже сами продукты)
            # """
                products = list(Product.objects.filter(id__in=CategoryProduct.objects.filter(category=Category.objects.get(title=category)).values('product')).values()[cls.clpages:cls.clpages+x])
            else:
                products = list(Product.objects.all().values()[cls.clpages:cls.clpages+x])
            if products:
                cls.clpages += len(products)
            data = { "items":products }
            print("loaded: ",cls.clpages)
            return JsonResponse(data, status=200)
        raise Http404

def product_detailsview(request):
    # [1:-1] убираю кавычки, они нужны чтоб можно было спокойно считывать пробелы
    product = request.GET.get('product', None)
    context = {
        "title": "Barsik Shop",
        "logedin": request.user.is_authenticated,
        "left_menu": Category.objects.order_by("title").all(),
        "product": Product.objects.get(title=product),
        "basket_items": request.session.get('basket', None),
    }
    return render(request, 'catalogue/product.html', context)


@login_required(login_url='login')
def basketview(request):
    products = Product.objects.filter(title__in=request.session.get('basket', ''))
    context = {
        "title": "Barsik Shop",
        "logedin": request.user.is_authenticated,
        "left_menu": Category.objects.order_by("title").all(),
        "sum_cost": sum([item.cost for item in products]),
        "basket_items": products,
    }
    return render(request, 'catalogue/basket.html', context)

@login_required(login_url='login')
def add_to_basketview(request):
    product = request.GET['item']
    if not 'basket' in request.session or not request.session['basket']:
        request.session['basket'] = [product]
    else:
        saved_list = request.session['basket']
        if product not in saved_list:
            saved_list.append(product)
            request.session['basket'] = saved_list
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def clear_basketview(request):
    try:
        del request.session['basket']
    except:
        pass
    return redirect('basket')
