# Generated by Django 3.1.1 on 2020-09-28 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0016_auto_20200918_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxes',
            name='box_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='boxes',
            name='warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bx_wh', to='inv.warehouse'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inv_comment',
            field=models.CharField(default='an inventory was conducted', max_length=500),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_owner_staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='inv.staff'),
        ),
        migrations.AlterField(
            model_name='items_in_boxes',
            name='moved_by_staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inv.staff'),
        ),
        migrations.AlterField(
            model_name='items_in_boxes',
            name='reason',
            field=models.CharField(default='add to database', max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_name',
            field=models.CharField(default='staff name', max_length=100),
        ),
    ]