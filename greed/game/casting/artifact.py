from game.casting.actor import Actor
from game.shared.point import Point
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""
        self._value = 0

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message
