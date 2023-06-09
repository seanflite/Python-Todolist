# Generated by Django 4.1.5 on 2023-01-13 07:25

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('completed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_items', to='tasks.todolist')),
            ],
        ),
    ]
