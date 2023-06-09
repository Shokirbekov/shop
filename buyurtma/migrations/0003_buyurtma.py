# Generated by Django 4.1.7 on 2023-04-14 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mahsulot_sotuvchi'),
        ('userapp', '0002_alter_profil_shahar'),
        ('buyurtma', '0002_delete_buyurtma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
    ]
