from __future__ import absolute_import

from .compat import include, url


urlpatterns = [
    url('', include('category.urls')),
]
