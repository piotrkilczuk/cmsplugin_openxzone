from cms.models import CMSPlugin
from django.db import models
from django_openx.zone import Zone

# see: /lib/OA/Dll/Zone.php
ZONE_TYPE_MAPPING = (
    'adjs',
    'adlayer',
)


class OpenXZonePlugin(CMSPlugin):
    zone_id = models.PositiveSmallIntegerField()

    # cache fields for data obtained via XML-RPC
    height = models.PositiveSmallIntegerField(default=0, editable=False)
    publisher_id = models.PositiveSmallIntegerField(default=0, editable=False)
    tag = models.TextField(editable=False)
    type = models.PositiveSmallIntegerField(default=0, editable=False)
    width = models.PositiveSmallIntegerField(default=0, editable=False)
    zone_name = models.CharField(max_length=255, editable=False)
    
    def __get_zone_dict(self):
        return Zone.get(self.zone_id)
    
    def __get_tag(self):
        # no idea why isn't the proper code returned, when requesting
        # generate_tag WITHOUT code_type
        try:
            code_type = ZONE_TYPE_MAPPING[self.type]
        except IndexError:
            code_type = ZONE_TYPE_MAPPING[0]
        return str(Zone.get(self.zone_id).generate_tag(code_type=code_type))

    def __unicode__(self):
        return 'Zone ' + str(self.zone_id)
    
    def save(self, *args, **kwargs):
        zone_dict = self.__get_zone_dict()
        self.height = zone_dict['height']
        self.publisher_id = zone_dict['publisher_id']
        self.type = zone_dict['type']
        self.width = zone_dict['width']
        self.zone_name = zone_dict['zone_name']
        self.tag = self.__get_tag()
        super(OpenXZonePlugin, self).save(*args, **kwargs)