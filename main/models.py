from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # Nama produk
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga produk
    description = models.TextField()  # Deskripsi produk

    def __str__(self):
        return self.name
