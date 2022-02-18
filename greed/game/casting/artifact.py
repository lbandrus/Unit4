from game.casting.actor import Actor
from game.shared.point import Point
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """An object that inherits from Actor. A Object that holds the methods and varibles in charge of 
    movement, color, messages and values for game play.  

    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
        Added on Artifact class:
            _message (string): Holds the message that can be displayed to the banner.
            _value (int): The point value of the artifact.

    """
    def __init__(self):
        """Inherits Actor and constructs a new Artifact."""
        super().__init__()
        self._message = ""
        self._value = 0

    def set_value(self, value):
        """Updates the point value of the Artifact.

        Args:
            value (int): The given point value."""
        self._value = value

    def get_value(self):
        """Retrives the point value of the Artifact.

        Returns:
            value (int): The artifact's point value."""
        return self._value

    def set_message(self, message):
        """Updates the point value of the Artifact.

        Args:
            value (string): The artifact's message."""
        self._message = message

    def get_message(self):
        """Retrives the message of the Artifact.

        Returns:
            value (string): The artifact's message."""
        return self._message