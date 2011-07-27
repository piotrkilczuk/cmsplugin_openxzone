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
            'js': instance.tag,
            'js_admin': instance.tag_admin,
            'zone': {
                'height': instance.height,
                'id': instance.zone_id, 
                'published_id': instance.publisher_id,
                'type': instance.type,
                'width': instance.width,
                'name': instance.zone_name,
            }
        })
        return context 

plugin_pool.register_plugin(CMSOpenXZonePlugin)