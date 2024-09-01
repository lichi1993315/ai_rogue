from components.ai import HostileEnemy
from components.fighter import Fighter

from entity import Actor

player = Actor(char="@", color=(255, 255, 255), name="Player", ai_cls=HostileEnemy, fighter=Fighter(hp=30, defense=2, power=5))

rabbit = Actor(char="r", color=(63, 127, 63), name="Rabbit", ai_cls=HostileEnemy, fighter=Fighter(hp=5, defense=0, power=2))

bear = Actor(char="B", color=(0, 127, 0), name="Bear", ai_cls=HostileEnemy, fighter=Fighter(hp=16, defense=1, power=4))