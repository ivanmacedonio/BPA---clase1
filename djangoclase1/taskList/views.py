from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        data = {"products": list(products.values())}
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Internal server error"}, status=400)

def product_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        data_title = data.get(
            "title",
        )
        data_description = data.get(
            "description",
        )
        data_used = data.get(
            "used",
        )
        data_price = data.get(
            "price",
        )

        if data_title and data_price:
            product = Product.objects.create(
                title=data_title,
                description=data_description,
                used=data_used,
                price=data_price,
            )
            return JsonResponse({"message": "product created succesfully"}, status=201)
        else:
            return JsonResponse({"error": "Internal server error"}, status=400)
    else:
        return JsonResponse({"Error": "Method not allowed"}, status=405)


def delete_products(request, id):
    product = Product.objects.filter(pk=id).first()
    if not product:
        return JsonResponse(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "DELETE":
        product.delete()
        return JsonResponse(
            {"message": "Product deleted succesfully"}, status=status.HTTP_202_ACCEPTED
        )
    else:
        return JsonResponse(
            {"error": "Interal server error"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
