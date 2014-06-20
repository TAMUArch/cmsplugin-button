from django.db import models
from cms.models import CMSPlugin



validate_link = RegexValidator(r'^(http|https)://',
    u"Enter a valid link beginning with http:// or https://",
    'invalid')

class ButtonPlugin(CMSPlugin):
    background = models.ImageField(blank=False, null=False,
            upload_to='cms/plugin/button')
    foreground = models.ImageField(blank=False, null=False,
            upload_to='cms/plugin/button')
    title = models.CharField(max_length=255, blank=False, null=False)
    link = models.CharField(max_length=255, blank=False, null=False,
            validators=[validate_link])

    def __unicode__(self):
        return u'Button - %s' % self.title

    @property
    def render_template(self):
        return 'cms/plugins/button/button.html'
