# Generated by Django 4.0 on 2022-01-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_product_description_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg', max_length=2000, verbose_name='image'),
        ),
    ]
