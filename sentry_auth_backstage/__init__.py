from __future__ import absolute_import

from sentry.auth import register

from .provider import BackstageOAuth2Provider

register('backstage', BackstageOAuth2Provider)
