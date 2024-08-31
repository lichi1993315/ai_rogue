import tcod
from pathlib import Path
import logging

ASSETS_DIR = Path(__file__) / "../assets"
logger = logging.getLogger(__name__)

def main() -> None:
    """Main entry point."""
    logging.basicConfig(level="DEBUG")
    TILESET = ASSETS_DIR / "Alloy_curses_12x12.png"
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(TILESET, 16, 16, tcod.tileset.CHARMAP_CP437)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="AI Dungeon",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="Hello, world!")
            context.present(root_console)

            for event in tcod.event.wait():
                context.convert_event(event)
                if event.type == "QUIT":
                    raise SystemExit


if __name__ == "__main__":
    main()