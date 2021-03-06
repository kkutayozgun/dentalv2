# Generated by Django 3.2 on 2022-04-05 19:30

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_frequentlyaskedquestion_frequentlyaskedquestiontranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowItWorksPageSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='about/banner', verbose_name='Banner Image')),
                ('meta_keywords', models.ManyToManyField(blank=True, to='page.Keywords', verbose_name='Meta Anahtar Kelimeler')),
            ],
            options={
                'verbose_name': 'How it works Page SEO',
                'verbose_name_plural': 'How it works Page SEO',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HowItWorksPageSeoTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Başlığı')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Açıklaması')),
                ('banner_title', models.CharField(max_length=200, verbose_name='Banner Title')),
                ('banner_description', models.TextField(blank=True, null=True, verbose_name='Banner Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='page.howitworkspageseo')),
            ],
            options={
                'verbose_name': 'How it works Page SEO Translation',
                'db_table': 'page_howitworkspageseo_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
