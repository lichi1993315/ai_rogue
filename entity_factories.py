from components.ai import HostileEnemy, InteractiveNPC
from components.fighter import Fighter

from entity import Actor

player = Actor(char="@", color=(255, 255, 255), name="Player", ai_cls=HostileEnemy, fighter=Fighter(hp=3000, defense=1, power=5))

rabbit = Actor(char="r", color=(63, 127, 63), name="Rabbit", ai_cls=InteractiveNPC, fighter=Fighter(hp=5, defense=0, power=2))

elephant = Actor(char="E", color=(0, 127, 0), name="Elephant", ai_cls=HostileEnemy, fighter=Fighter(hp=16, defense=1, power=4))

lion = Actor(char="L", color=(68, 127, 0), name="Lion", ai_cls=HostileEnemy, fighter=Fighter(hp=16, defense=2, power=8))