from __future__ import unicode_literals
from django.db import models

# Create your models here.


class ProductManager(models.Manager):
    def create_new_product(self, product_data):
        errors = []

        if not product_data['name']:
            errors.append("Name can not be blank.")
        if not product_data['description']:
            errors.append("Description can not be blank")
        if not product_data['price']:
            errors.append("Price can not be blank.")

        response = {}

        if errors:
            response['errors'] = errors
            response['created'] = False
        else:
            new_product = self.create(name=product_data['name'], description=product_data['description'], price=product_data['price'])
            response['created'] = True
            response['new_product'] = new_product
        return response

    def update_product(self, id, product_data):
        errors = []

        if not product_data['name']:
            errors.append("Name can not be blank.")
        if not product_data['description']:
            errors.append("Description can not be blank")
        if not product_data['price']:
            errors.append("Price can not be blank.")

        response = {}
        if errors:
            response['errors'] = errors
            response['updated'] = False
        else:
            product = self.get(id=id)
            product.name = product_data['name']
            product.description = product_data['description']
            product.price = product_data['price']
            product.save()
            response['updated'] = True
            response['updated_product'] = product
        return response


class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
