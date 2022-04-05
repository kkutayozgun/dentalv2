from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin
from page.models import (Keywords, HomeSlider, seo_translations, HomePageSeo, ServiceCategory, ServiceItem,
                         ServicesPageSeo, BeforeAfterImage, AboutPageSeo, FrequentlyAskedQuestion, HowItWorksPageSeo)

admin.site.register(Keywords, TranslatableAdmin)

seo_fields = tuple(seo_translations.keys()) + ("meta_keywords",)


@admin.register(HomeSlider)
class HomeSliderAdmin(TranslatableAdmin):
    search_fields = ('title',)
    list_display = ('title', 'redirect_url',)
    fields = ('title', 'description', 'redirect_url', 'image')


@admin.register(HomePageSeo)
class HomePageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


@admin.register(ServicesPageSeo)
class ServicesPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Category Information"), {'fields': ('name', 'slug', 'description', 'icon', 'in_home')}),
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('name', 'icon', 'in_home')
    list_editable = ('icon', 'in_home')
    list_filter = ('icon', 'in_home')
    search_fields = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',),
        }


@admin.register(ServiceItem)
class ServiceItemAdmin(TranslatableAdmin):
    fieldsets = (
        (None,
         {'fields': ('banner_title', 'slug', 'category', 'banner_description', 'content', 'image', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title', 'slug', 'category')
    list_filter = ('category',)
    search_fields = ('banner_title',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('banner_title',)
        }


@admin.register(BeforeAfterImage)
class BeforeAfterImageAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutPageSeo)
class AboutPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Content 1"), {'fields': ('content_title1', 'content_body1', 'content_image1')}),
        (_("Content 2"), {'fields': ('content_title2', 'content_body2', 'content_image2')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(HowItWorksPageSeo)
class HowItWorksPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(TranslatableAdmin):
    fields = ('question', 'answer')
    list_display = ('question',)
