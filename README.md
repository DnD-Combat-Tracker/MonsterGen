# MonsterGen

MonsterGen is based on Fortuna and Storm by Robert Sharp.
- Fortuna: Random Value Toolkit for Generative Modeling.
- Storm: High-performance Random Number Engine.


## Installation
```shell script
$ pip install MonsterGen
```

## Monster Class
`Monster(cr) -> Monster`

```python
from MonsterGen import Monster, CR

monster_cr = CR(10)
print(Monster(monster_cr))
```

```
Name: Wraith
CR: 10
Hit Points: 217
Armor Class: 15
Attack Bonus: 9
Typical Damage: 63 - 68
Save DC: 16
XP Value: 5900
```

## CR Class
`CR(cr) -> CR`
- cr: int, -3 to 30

The CR class is a numeric system representing the relative power of a monster in D&D 5e.
This system is a bit funky with values below 1, be careful... here be dragons!
CR less than 1 are printed as fractions but valued mathematically as integers [-3, 0]. See below:

#### CR Mapping

```python
from MonsterGen import CR

print(f"CR: {CR(-3)}")
print(f"CR: {CR(-2)}")
print(f"CR: {CR(-1)}")
print(f"CR: {CR(0)}")
print(f"CR: {CR(1)}")
print(f"CR: {CR(2)}")
print(f"CR: {CR(3)}")
print('...')
print(f"CR: {CR(30)}")
```

```
CR: 1/16
CR: 1/8
CR: 1/4
CR: 1/2
CR: 1
CR: 2
CR: 3
...
CR: 30
```

### Party Adapter Method (Factory Function)
`CR.player_adapter(average_level, num_players=5, difficulty=0) -> CR`

Class method for computing CR from party composition and difficulty setting.
- average_level: int, 1 to 20
- num_players: int, 1 to 9
- difficulty: int, -5 to 5 
    - Stupid Easy: -5 to -4
    - Easy: -3 to -2
    - Normal: -1 to 1
    - Epic: 2 to 3
    - Legendary: 4 to 5

## Npc Class
`Npc() -> Npc`

Produces a random NPC.

```python
from MonsterGen import Npc

print(Npc())
```

```
Profession: Bookbinder
Race: Tiefling
Background: Soldier
Appearance: Flamboyant or outlandish clothes
Mannerism: Speaks in rhyme
Hit Points: 8
Armor Class: 11
Damage: 1
```

## random_trap function
`random_trap(cr, dam_type=None) -> Trap`
- cr: int, -3 to 30
- dam_type: str, ['bludgeoning', 'falling', 'piercing', 'slashing', 'poison', 'acid', 'fire', 'lightning', 'cold', 'necrotic']

Produces a random trap. If `dam_type` is None it will choose a random damage type.

```python
from MonsterGen import random_trap

print(random_trap(10, dam_type="falling"))
```

```
Name: Greased Slide
Type: Dangerous Trap
CR: 10
Spot & Disarm: DC: 12
Save vs: CON DC 15 for half damage
Damage: 3d6 falling
Disarm XP: 5900
```

## monster_loot function
`monster_loot(cr) -> Loot`
- cr: int, -3 to 30

Produces random treasure for a single monster. Typically this is just coinage.
```python
from MonsterGen import monster_loot

print(monster_loot(10))
```

```
Copper Coins: 1800
Electrum Coins: 50
```

## horde_loot function
`horde_loot(cr) -> Loot`
- cr: int, -3 to 30

Produces random treasure for a boss or horde of monsters. High-quality loot with magic items appropriate to the CR.

```python
from MonsterGen import horde_loot

print(horde_loot(10))
```

```
Copper Coins: 400
Silver Coins: 7000
Gold Coins: 2200
Platinum Coins: 140
Jewels: 50 GP
Oil of etherealness
Quaal's feather token
```
