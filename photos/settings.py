# -*- coding: utf-8 -*-
from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)


SWEARWORDS = getattr(settings, 'PROJECT_SWEARWORDS', [])
