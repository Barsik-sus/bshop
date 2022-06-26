from django.urls import path

from .views import *

urlpatterns = [
    path('', CatalogueView.index, name="home"),
    #path('login', login),
    # TODO: Переименовать. Должно показывать товары выбранной категории
    path('catalogue/<slug:category>/', CatalogueView.index),
    # path('load/', CatalogueView.loadview, name="loadview"),
    path('basket/', basketview, name="basket"),
    path('details/', product_detailsview, name="product_details"),
    path('add_to_basket/', add_to_basketview, name="atb"),
    path('clear_basket/', clear_basketview, name="clear_basket"),
]