from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from button.models import ButtonPlugin



class CMSButtonPlugin(CMSPluginBase):
    model = ButtonPlugin
    name = _('Button Plugin')
    render_template = 'cms/plugins/button/button.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance})
        return context

plugin_pool.register_plugin(CMSButtonPlugin)
