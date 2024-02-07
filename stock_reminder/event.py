class Event:
    """A generic class that provides signal/slot functionality"""

    def __init__(self):
        self.listeners = []

    def connect(self, listener):
        self.listeners.append(listener)

    def fire(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)


class Mock:
    def __init__(self):
        self.called = False
        self.params = ()

    def __call__(self, *args, **kwargs):
        self.called = True
        self.params = (args, kwargs)