import pyvkontakte
from vkontakte_gui import cache
from vkontakte_gui import settings


def api():
    """
    :rtype: pyvkontakte.VkontakteApi
    """
    api = cache.vkontakte['api']
    if not api:
        raise ValueError('Api not set')
    return api


def login(login, password):
    api = pyvkontakte.VkontakteApi.auth(login, password, settings.CLIENT_ID, settings.SCOPE)
    cache.vkontakte['api'] = api
    cache.vkontakte['access_token'] = api.access_token
    return api
