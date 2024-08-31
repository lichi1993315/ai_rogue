# AI规则怪谈

## 游戏简介
本游戏是以美式桌游为核心形式，以aigc为剧本驱动的冒险解密游戏。

玩家将会在动物园规则怪谈（暂定）的世界观下自由探索，搜集线索、道具并逃离动物园。

## 设计目的
1. 验证aigc生成游戏剧情的可行性
2. 探索哪些世界观和玩法系统是易于aigc的
3. 验证玩法的有趣性
4. 评估资产量和开发难度


## 游戏玩法以及流程
1. 玩家开局可以选择一个游戏人物和一个npc，不同人物拥有不同的属性，性格和初始道具。
2. 开局后，程序生成地图，ai会根据地图信息，提供一系列出生点让玩家选择。
3. 正式的游戏分为三个阶段，玩家行动，敌人行动，环境。
4. 玩家行动阶段包含调查、使用道具，移动三种类型。
  1. 调查时，玩家可以对身边的npc进行询问，或者调查周围建筑物、房间、物体的信息。这个阶段随着玩家的行为可能获得一些道具，状态，以及关键剧情点。例如调查冰箱可能会出现食物类道具，而食物类道具可以恢复hp。具体物体描述和物体名称由ai确定。
  2. 使用道具时，ai会根据规则书中的设定判断道具效果。
  3. 初始时，地图并不完全开放，而是由程序化生成随机地图，将部分连通点加锁。钥匙散落在可达区域。需要探索后得到钥匙。
5. 敌人行动阶段，包括移动和攻击和技能三种。只有一些boss拥有技能。比如兔子会让玩家之后三回合内看到的一切都变成胡萝卜。
6. 环境阶段，会根据当前剧情进度来自动触发一些效果。例如，当玩家击杀一个敌人时，在随机地点生成一个杏仁水。
7. 游戏胜利：玩家成功逃离动物园，或者找到某一个真相。
8. 游戏失败：当玩家的san值为0时，或者hp为0时，游戏失败。

## 开发引擎
- 基于python的libtcod引擎
- python版本：3.11
- AI版本：GPT4o

