# coding= utf-8

from django.db import models


class TenderTypes(models.Model):
    """
    # Типы заявок: ремонт, профилактика, замена ЭКЛЗ.
    """

    nametendertypes = models.CharField(u'вид заявки',
                      max_length=255, unique=True)

    def __unicode__(self):
        return self.nametendertypes

    class Meta:
        verbose_name_plural = u'виды заявок'
        app_label = 'base_structure'
        verbose_name = u'вид заявки'
