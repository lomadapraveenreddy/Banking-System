# Generated by Django 3.0.6 on 2020-06-03 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_customer_accountnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaintID', models.CharField(max_length=15, unique=True)),
                ('dateTime', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(max_length=180)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Transaction')),
            ],
        ),
    ]
