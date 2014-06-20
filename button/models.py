from django.db import models
from cms.models import CMSPlugin



class ButtonPlugin(CMSPlugin):
    background = models.ImageField(blank=False, null=False)
    foreground = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    link = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return u'Button - %s' % self.title

    @property
    def render_template(self):
        return 'cms/plugins/button/button.html'
