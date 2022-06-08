# Generated by Django 3.2.10 on 2022-06-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0003_alter_book_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_name', models.CharField(max_length=50, verbose_name='IndexName')),
                ('text', models.TextField(verbose_name='Text')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to='library.book')),
            ],
        ),
    ]
