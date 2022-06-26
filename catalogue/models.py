from django.db import models

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
# gd_storage = GoogleDriveStorage()

class Product(models.Model):
    title = models.CharField("title", default="Unnamed", max_length=50)
    description = models.TextField('description')
    # image = models.ImageField(upload_to='products', storage=gd_storage, default='/static/img/image_not_found.jpg')
    image = models.CharField("image", default="https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg", max_length=2000)
    cost = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField("title", default="Unnamed", max_length=50)

    def __str__(self) -> str:
        return self.title

class CategoryProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.category) + " - " + str(self.product)
