# Generated by Django 4.1.7 on 2023-04-17 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_profil_shahar'),
        ('buyurtma', '0004_savatitem_remove_savat_mahsulot_remove_savat_miqdor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savatitem',
            name='yetkazish_puli',
            field=models.PositiveIntegerField(default=15000),
        ),
        migrations.AlterField(
            model_name='savatitem',
            name='savat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlari', to='buyurtma.savat'),
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holat', models.CharField(blank=True, choices=[("To'lanishi kutilmoqda", "To'lanishi kutilmoqda"), ('Yetkazilishi kutilmoqda', 'Yetkazilishi kutilmoqda'), ('Yetkazilyapti', 'Yetkazilyapti'), ('Yetkazildi', 'Yetkazildi'), ('Qabul qilingan', 'Qabul qilingan')], max_length=500)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('summa', models.IntegerField()),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
                ('savat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat')),
            ],
        ),
    ]
