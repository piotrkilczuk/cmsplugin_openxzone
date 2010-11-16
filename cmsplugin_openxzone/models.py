from cms.models import CMSPlugin
from django.db import models
from django_openx.zone import Zone


class OpenXZonePlugin(CMSPlugin):
    zone_id = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return 'Zone ' + str(self.zone_id)
    
    def get_tag(self):
        """Return javascript zone as string representation"""
        try:
            js = self.get_zone_dict().generate_tag()
        except AttributeError:
            js = ''
        return js
    
    def get_zone_dict(self):
        return Zone.get(self.zone_id)