# Generated by Django 4.2.1 on 2024-08-31 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_remove_post_pub_date_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.user')),
            ],
        ),
    ]
