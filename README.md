# MonsterGen

```shell script
$ pip install MonsterGen
```
```python
from MonsterGen import Monster

print(Monster(10))
```

```
Name: Displacer Beast
CR: 10
Hit Points: 217
Armor Class: 17
Attack Bonus: 7
Typical Damage: 63 - 68
Save DC: 16
XP Value: 5900
```

## Alternative Calling Signatures
```python
from MonsterGen import Monster, CR

monster_cr = CR.party_adapter(average_level=10, num_players=3, difficulty=0)
print(Monster(monster_cr))
```

```
Name: Wyvern
CR: 10
Hit Points: 214
Armor Class: 18
Attack Bonus: 6
Typical Damage: 63 - 68
Save DC: 16
XP Value: 5900
```
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
