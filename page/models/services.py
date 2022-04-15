from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class ServicesPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Title"), max_length=200, blank=True, null=True),
        banner_description=RichTextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("Service Page SEO")
        verbose_name_plural = _("Service Page SEO")


class ServiceCategory(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    class ServiceCategoryIcons(models.Choices):
        MICROSCOPE = "fa-microscope"
        TEETH = "fa-teeth"
        BONE_BREAK = "fa-bone-break"
        SCALPEL_PATH = "fa-scalpel-path"
        HEAD_SIDE_BRAIN = "fa-head-side-brain"
        HEARTH_RATE = "fa-heart-rate"

    translations = TranslatedFields(
        name=models.CharField(_("Category Name"), max_length=200),
        slug=models.SlugField(_("Slug"), max_length=200),
        description=models.TextField(_("Description"), blank=True, null=True),
        banner_title=models.CharField(_("Title"), max_length=200, blank=True, null=True),
        banner_description=RichTextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    icon = models.CharField(_("Category Icon"), max_length=50,
                            choices=ServiceCategoryIcons.choices, blank=True, null=True)
    in_home = models.BooleanField(_("In home page services section?"), default=False)
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")

    def __str__(self):
        return self.name


class ServiceItem(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Title"), max_length=200),
        banner_description=RichTextField(_("Description"), blank=True, null=True),
        slug=models.SlugField(_("Slug"), max_length=200),
        content=RichTextUploadingField(_("Content Body 1"), blank=True, null=True),
        **seo_translations
    )
    category = models.ForeignKey(ServiceCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name=_("Kategori"))
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)
    image = models.ImageField(_("Service Image"), upload_to="services", blank=True, null=True)

    class Meta:
        verbose_name = _("Service Item")
        verbose_name_plural = _("Service Items")

    def __str__(self):
        return self.banner_title
