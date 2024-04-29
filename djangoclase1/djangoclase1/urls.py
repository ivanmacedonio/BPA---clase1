from django.contrib import admin
from django.urls import path
from taskList.views import product_list, product_create, delete_products

urlpatterns = [
    path("", admin.site.urls),
    path("tasks", product_list, name="products_view"),
    path("create_tasks/hola", product_create, name="products_view"),
    path("delete_tasks/<int:id>", delete_products, name="products_delete"),
]
