from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    product_description = models.CharField(max_length=300, default=None, blank=True, null=True)
    suggestion_image = models.FileField(null=True)
    second_image = models.FileField(null=True)
    PRODUCT_TYPE_CHOICES = [
        ('hamburguer', 'Hamburguer'),
        ('salgado', 'Salgado'),
        ('doce', 'Doce'),
    ]
    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPE_CHOICES,
    )

    def __str__(self):
        return self.product_name
