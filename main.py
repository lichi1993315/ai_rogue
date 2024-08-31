import tcod
from pathlib import Path
import copy

from ai_rogue.procgen import generate_dungeon
from engine import Engine
import entity_factories
from input_handlers import EventHandler
from entity import Entity

ASSETS_DIR = Path(__file__) / "../assets"

def main() -> None:
    """Main entry point."""
    TILESET = ASSETS_DIR / "Alloy_curses_12x12.png"
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 50

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(TILESET, 16, 16, tcod.tileset.CHARMAP_CP437)

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player,
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)


    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="AI规则怪谈",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            engine.handle_events(tcod.event.wait())

if __name__ == "__main__":
    main()