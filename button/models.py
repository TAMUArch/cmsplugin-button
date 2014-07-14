from django.db import models
from django.core.validators import RegexValidator

from cms.models import CMSPlugin



class ButtonPlugin(CMSPlugin):
    foreground = models.ImageField(blank=False, null=True,
            upload_to='cms/plugin/button',
            verbose_name='Foreground Image')
    background = models.ImageField(blank=False, null=True,
            upload_to='cms/plugin/button',
            verbose_name='Background Image',
            help_text='Shown on hover')
    title = models.CharField(max_length=255, blank=False, null=True)
    link = models.CharField(max_length=255, blank=False, null=True)

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def render_template(self):
        return 'cms/plugins/button/button.html'
