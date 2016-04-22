import pyvkontakte
from vkontakte_gui import cache
from vkontakte_gui import settings
from vkontakte_gui.utils.vkontakte import VkontakteApi


def api():
    """
    :rtype: vkontakte_gui.utils.vkontakte.VkontakteApi
    """
    api = cache.vkontakte['api']
    if not api:
        raise ValueError('Api not set')
    return api


def login(login, password):
    auth_data = pyvkontakte.auth(login, password, settings.CLIENT_ID, settings.SCOPE)
    cache.vkontakte['api'] = VkontakteApi(auth_data['access_token'])
    cache.vkontakte['access_token'] = auth_data['access_token']
    return api
