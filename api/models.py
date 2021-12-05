from django.db import models
from django.utils.translation import gettext as _


class TextClassification(models.Model):
    url = models.CharField(_('Url'), null=True, blank=True, max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)
    flag = models.BooleanField(_('Flag'), null=True, blank=True, default=False)
    status = models.CharField(_('Status'), null=True, blank=True, max_length=255)
    tag = models.CharField(_('Tag'), null=True, blank=True, max_length=255)
    label = models.CharField(_('Label predict'), blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = 'Text classification'
        verbose_name_plural = 'Texts classifications'
