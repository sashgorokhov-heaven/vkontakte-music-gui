from kivy.adapters.listadapter import ListAdapter
from vkontakte_gui.widgets import AudioWidget


class MusicListAdapter(ListAdapter):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('data', [])
        kwargs.setdefault('cls', AudioWidget)
        kwargs.setdefault('selection_mode', 'multiple')
        kwargs.setdefault('args_converter', AudioWidget.args_converter)
        super(MusicListAdapter, self).__init__(**kwargs)

    def add_data(self, data):
        self.data.append(data)
        return self.create_view(len(self.data) - 1)
