from urllib import urlencode

import pyvkontakte
from kivy.network.urlrequest import UrlRequest


class VkontakteApi(pyvkontakte.VkontakteApi):
    def call(self, method, on_success=None, on_error=None, **kwargs):
        params = self._params_encode(**kwargs)
        query = urlencode(params)
        url = self.base_url + method + '?' + query
        return UrlRequest(url, on_success=on_success, on_error=on_error)