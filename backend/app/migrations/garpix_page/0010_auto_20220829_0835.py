# Generated by Django 3.1 on 2022-08-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_page', '0009_basecomponent_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecomponent',
            name='text_title_de',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='basecomponent',
            name='text_title_ru',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='basecomponent',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='basecomponent',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_author_de',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='SEO автор (author)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_author_ru',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='SEO автор (author)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_description_de',
            field=models.TextField(blank=True, default='', null=True, verbose_name='SEO описание (description)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_description_ru',
            field=models.TextField(blank=True, default='', null=True, verbose_name='SEO описание (description)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_keywords_de',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='SEO ключевые слова (keywords)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_keywords_ru',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='SEO ключевые слова (keywords)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_title_de',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='SEO заголовок страницы (title)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='seo_title_ru',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='SEO заголовок страницы (title)'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]