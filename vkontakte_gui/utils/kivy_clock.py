import collections
import kivy.clock

schedule = lambda func, *args, **kwargs: kivy.clock.Clock.schedule_once(lambda _: func(*args, **kwargs))


def async_execute(iterator, _firstrun=True):
    if callable(iterator):
        def wrapper(*args, **kwargs):
            return async_execute(iterator(*args, **kwargs))
        return wrapper
    if not isinstance(iterator, collections.Iterator):
        iterator = iter(iterator)
    if _firstrun or next(iterator, False):
        schedule(async_execute, iterator, False)
