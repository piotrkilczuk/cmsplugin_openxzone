from cms.models import CMSPlugin
from django.db import models
from django_openx.zone import Zone
import uuid

# see: /lib/OA/Dll/Zone.php
# Zone.get().type to generate_tag(code_type) mapping
ZONE_TYPE_MAPPING = (
    'adjs',
    'adlayer',
)
# same as ZONE_TYPE_MAPPING, but adds possibility 
# to render the zone using other rendering mode when in admin edit mode
ADMIN_ZONE_TYPE_MAPPING = (
    'adjs',
    'adjs',
)


class OpenXZonePlugin(CMSPlugin):
    zone_id = models.PositiveSmallIntegerField()

    # cache fields for data obtained via XML-RPC
    height = models.PositiveSmallIntegerField(default=0, editable=False)
    publisher_id = models.PositiveSmallIntegerField(default=0, editable=False)
    tag = models.TextField(editable=False)
    tag_admin = models.TextField(editable=False)
    type = models.PositiveSmallIntegerField(default=0, editable=False)
    width = models.PositiveSmallIntegerField(default=0, editable=False)
    zone_name = models.CharField(max_length=255, editable=False)
    
    def __get_zone_dict(self):
        return Zone.get(self.zone_id)
    
    def __get_tag(self, admin=False, params=['layerstyle=simple']):
        # no idea why isn't the proper code returned, when requesting
        # generate_tag WITHOUT code_type
        d = ADMIN_ZONE_TYPE_MAPPING if admin else ZONE_TYPE_MAPPING
        try:
            code_type = d[self.type]
        except IndexError:
            code_type = d[0]
        tag = str(Zone.get(self.zone_id).generate_tag(code_type=code_type,
                                                      params=params))
        return tag.replace('INSERT_RANDOM_NUMBER_HERE', str(uuid.uuid1()))

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
        self.tag_admin = self.__get_tag(admin=True)
        super(OpenXZonePlugin, self).save(*args, **kwargs)