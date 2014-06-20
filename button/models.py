from django.db import models
from django.core.validators import RegexValidator

from cms.models import CMSPlugin



validate_link = RegexValidator(r'^(http|https)://',
    u"Enter a valid link beginning with http:// or https://",
    'invalid')

class ButtonPlugin(CMSPlugin):
    foreground = models.ImageField(blank=False, null=False,
            upload_to='cms/plugin/button',
            verbose_name='Foreground Image')
    background = models.ImageField(blank=False, null=False,
            upload_to='cms/plugin/button',
            verbose_name='Background Image',
            help_text='Shown on hover')
    title = models.CharField(max_length=255, blank=False, null=False)
    link = models.CharField(max_length=255, blank=False, null=False,
            validators=[validate_link])

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def render_template(self):
        return 'cms/plugins/button/button.html'
