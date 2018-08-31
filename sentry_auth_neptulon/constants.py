from __future__ import absolute_import, print_function

from django.conf import settings

ACCESS_TOKEN_URL = getattr(settings, 'BACKSTAGE_TOKEN_URL', None)
AUTHORIZE_URL = getattr(settings, 'BACKSTAGE_AUTH_URL', None)
CLIENT_ID = getattr(settings, 'BACKSTAGE_CLIENT_ID', None)
CLIENT_SECRET = getattr(settings, 'BACKSTAGE_CLIENT_SECRET', None)
USER_DETAILS_ENDPOINT = getattr(settings, 'BACKSTAGE_USER_DETAILS_URL', None)

SCOPE = 'email'
