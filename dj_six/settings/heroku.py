from __future__ import absolute_import

import dj_database_url

from .common import *

DATABASES = {
    'default': dj_database_url.config()
}
