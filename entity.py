from typing import Tuple

class Entity:
    """
        A class to represent an entity in the game.

        Attributes:
        ----------
        x : int
            The x-coordinate of the entity.
        y : int
            The y-coordinate of the entity.
        char : str
            The character representing the entity.
        color : Tuple[int, int, int]
            The color of the entity in RGB format.
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

