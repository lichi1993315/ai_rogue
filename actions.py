from __future__ import annotations
from logger import logger
from typing import Optional, Tuple, TYPE_CHECKING
import color


if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity, Actor

class Action:
    def __init__(self, entity: Actor) -> None:
        super().__init__()
        self.entity = entity

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine

    def perform(self) -> None:
        """
        Perform this action with the objects needed to determine its scope.

        `self.engine` is the scope this action is being performed in.

        `self.entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()

class EscapeAction(Action):
    def perform(self) -> None:
        raise SystemExit()

class WaitAction(Action):
    def perform(self) -> None:
        pass

class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int):
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self) -> Tuple[int, int]:
        """Return the destination coordinates of this action"""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this actions destination"""
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination"""
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self) -> None:
        raise NotImplementedError()

class InteractAction(ActionWithDirection):
    def perform(self) -> None:
        target = self.target_actor
        if not target:
            return # No entity to interact with.

        logger.debug(f"{self.entity.name.capitalize()} interacts with {target.name}.")
        self.engine.chat_log.add_message(f" Hello {self.entity.name.capitalize()}, I am {target.name}. Do not run away!", fg=color.white)
        self.entity.fighter.start_conversation()

class MeleeAction(ActionWithDirection):
    def perform(self) -> None:
        target = self.target_actor
        if not target:
            return # No entity to interact with.

        damage = self.entity.fighter.power - target.fighter.defense

        attack_desc = f"{self.entity.name.capitalize()} melee attacks {target.name}"

        if self.entity is self.engine.player:
            attack_color = color.player_atk
        else:
            attack_color = color.enemy_atk

        if damage > 0:
            logger.debug(f"{attack_desc} for {damage} hit points.")
            self.engine.message_log.add_message(f"{attack_desc} for {damage} hit points.", fg=attack_color)
            target.fighter.hp -= damage
        else:
            logger.debug(f"{attack_desc} but does no damage.")
            self.engine.message_log.add_message(f"{attack_desc} but does no damage.", fg=attack_color)



class MovementAction(ActionWithDirection):
    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            logger.debug(f"({dest_x}, {dest_y}) is out of bounds.")
            self.engine.message_log.add_message("You cannot move there.", fg=color.yellow)
            return # Destination is out of bounds.
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            logger.debug(f"({dest_x}, {dest_y}) is blocked by a wall.")
            self.engine.message_log.add_message("You cannot walk into the wall.", fg=color.yellow)
            return # Destination is blocked by a tile.
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            blocked_entity = self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
            logger.debug(f"({dest_x}, {dest_y}) is blocked by an entity {blocked_entity.name}.")
            return

        self.entity.move(self.dx, self.dy)

class BumpAction(ActionWithDirection):
    def perform(self) -> None:
        if self.target_actor:
            return InteractAction(self.entity, self.dx, self.dy).perform()
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()

