from kivy.app import App
from vkontakte_gui.screens import get_screen_manager

__all__ = ['VkontakteMusic', 'root_app']


class VkontakteMusic(App):

    def build(self):
        self.title = 'Vkontakte Music'
        return get_screen_manager()
