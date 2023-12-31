# Generated by Django 3.0.14 on 2023-08-09 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('type', models.IntegerField(choices=[(1, 'Expense'), (2, 'Transaction')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('phoneNumber', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Invited')], default=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserExpense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('share', models.FloatField()),
                ('type', models.IntegerField(choices=[(1, 'Paid'), (2, 'Hadtopay')])),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplitwiseApp.Expense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplitwiseApp.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('desc', models.CharField(max_length=255)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Admin', to='SplitwiseApp.User')),
                ('members', models.ManyToManyField(to='SplitwiseApp.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='expense',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SplitwiseApp.User'),
        ),
        migrations.AddField(
            model_name='expense',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SplitwiseApp.Group'),
        ),
    ]
