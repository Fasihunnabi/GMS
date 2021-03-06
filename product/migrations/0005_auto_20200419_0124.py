# Generated by Django 3.0.4 on 2020-04-18 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_type',
            field=models.CharField(choices=[('Electrician', 'Electrician'), ('Mechanic', 'Mechanic')], max_length=20),
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(choices=[('Voltage', 'Voltage'), ('Oil level', 'Oil level'), ('Temperature', 'Temperature')], max_length=20)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Device')),
            ],
        ),
        migrations.CreateModel(
            name='sensor_reading_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Sensors')),
            ],
        ),
    ]
