from kivy.uix.label import Label


class AudioWidget(Label):
    @staticmethod
    def args_converter(index, item):
        return {'text': item['artist'] + '-' + item['title'], 'size_hint_y': None, 'height': 20}
