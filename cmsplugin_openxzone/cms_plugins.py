from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import models


class CMSOpenXZonePlugin(CMSPluginBase):
    model = models.OpenXZonePlugin
    name = _('OpenX banner zone')
    render_template = "cmsplugin_openxzone/zone.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'js': instance.get_tag(),
            'zone': instance.get_zone_dict(),
        })
        return context 

plugin_pool.register_plugin(CMSOpenXZonePlugin)


#def openx(request):
#    """Adds OpenX zone information to context
#    
#    Could possibly be refactored to allow distinction between 
#    """
#    
#    import django_openx as openx
#    
#    ctx = {}
#    publisher = openx.Publisher.get(2)
#    for zone in publisher.zones:
#        ctx[zone.zoneId] = zone.generate_tag()
#    return {'OPENX_ZONES': ctx}