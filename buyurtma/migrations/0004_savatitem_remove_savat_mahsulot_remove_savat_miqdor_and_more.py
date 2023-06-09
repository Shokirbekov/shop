# Generated by Django 4.1.7 on 2023-04-17 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mahsulot_sotuvchi'),
        ('buyurtma', '0003_buyurtma'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavatItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('yetkazish_kuni', models.PositiveSmallIntegerField()),
                ('umumiy_summa', models.IntegerField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mahsulot')),
            ],
        ),
        migrations.RemoveField(
            model_name='savat',
            name='mahsulot',
        ),
        migrations.RemoveField(
            model_name='savat',
            name='miqdor',
        ),
        migrations.RemoveField(
            model_name='savat',
            name='yetkazish_kuni',
        ),
        migrations.AddField(
            model_name='savat',
            name='sana',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Buyurtma',
        ),
        migrations.AddField(
            model_name='savatitem',
            name='savat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat'),
        ),
    ]
