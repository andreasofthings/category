try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

try:
    import json
except ImportError:
    from django.utils import simplejson as json

from django.conf.urls import url, include
