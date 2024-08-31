from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")

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

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
    ) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def spawn(self: T, game_map: GameMap, x: int, y: int) -> T:
        """
            Spawn a copy of this entity at the given location.

            Parameters:
            -----------
            game_map : GameMap
                The game map where the entity will be spawned.
            x : int
                The x-coordinate of the entity.
            y : int
                The y-coordinate of the entity.

            Returns:
            --------
            T
                The spawned entity.
        """
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        game_map.entities.add(clone)
        return clone

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

