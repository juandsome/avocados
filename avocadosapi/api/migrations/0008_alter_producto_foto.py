# Generated by Django 4.1.7 on 2023-03-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_producto_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="foto",
            field=models.ImageField(upload_to=""),
        ),
    ]