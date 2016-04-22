import logging

from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

from vkontakte_gui import services
from vkontakte_gui.services import api

_screen_manager = None

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

__all__ = ['LoginScreen', 'MusicListScreen', 'get_screen_manager']


class ScreenBase(Screen):
    def __init__(self, **kwargs):
        super(ScreenBase, self).__init__(**kwargs)
        self.name = self.__class__.__name__
        self.build()

    def build(self):
        pass


class LoginScreen(ScreenBase):
    def build(self):
        layout = GridLayout()
        layout.rows = 2

        self.error_layout = GridLayout(size_hint_y=None)
        self.error_layout.rows = 1
        layout.add_widget(self.error_layout)

        login_layout = GridLayout()
        login_layout.cols = 2
        login_layout.rows = 3

        login_layout.add_widget(Label(text='Login'))

        self.login_input = TextInput()
        login_layout.add_widget(self.login_input)
        login_layout.add_widget(Label(text='Password'))

        self.password_input = TextInput(password=True)
        login_layout.add_widget(self.password_input)

        login_button = Button(text='Login')
        login_button.bind(on_press=self.login)
        login_layout.add_widget(login_button)

        layout.add_widget(login_layout)
        self.add_widget(layout)

    def login(self, button):
        login = self.login_input.text.strip()
        password = self.password_input.text.strip()
        logger.debug('%s %s', login, password)
        if not login or not password:
            logger.debug('Empty login or password')
            return
        try:
            services.login(login, password)
        except Exception as e:
            logger.exception('Error while login')
            self.show_error(e)
            return

        screen_manager = get_screen_manager()
        screen_manager.current = 'MusicListScreen'

    def show_error(self, e):
        self.error_layout.clear_widgets()
        self.error_layout.add_widget(Label(text=e.message))


class MusicListScreen(ScreenBase):
    fist_enter = True

    def build(self):
        self.layout = GridLayout()
        self.layout.cols = 1
        self.add_widget(self.layout)

    def on_enter(self, *args):
        if self.fist_enter:
            Clock.schedule_once(self.load_music, 2)
            self.fist_enter = False

    def load_music(self, dt):
        self.layout.clear_widgets()
        music_list = api().call('audio.get')['items']
        for audio in music_list:
            self.layout.add_widget(Label(text=audio['artist'] + '-' + audio['title']))


def get_screen_manager():
    global _screen_manager
    if _screen_manager is None:
        _screen_manager = ScreenManager()
        _screen_manager.add_widget(LoginScreen())
        _screen_manager.add_widget(MusicListScreen())
    return _screen_manager
