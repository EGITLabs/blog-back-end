# Generated by Django 3.2.11 on 2024-07-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('UNDERSTANDING_CONCEPTS', 'Understanding Concepts in AI'), ('AI_IN_EDUCATION', 'AI in Education'), ('AI_IN_NEWS', 'AI in News/Trends'), ('SAFETY_AND_ETHICS', 'Safety and Ethics of AI')], default=('UNDERSTANDING_CONCEPTS', 'Understanding Concepts in AI'), max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
