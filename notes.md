# MonsterGen Primary API

### Monsters
- Monster(CR.party_adapter(average_level, num_players, difficulty))
    - average_level: required int, clamped range: 1 to 20
    - num_players: optional int, clamped range: 1 to 9
    - difficulty: optional int, clamped range: -5 to 5

### Treasure
- monster_loot(cr)
    - cr: required int, range: -3 to 30
- horde_loot(cr)
    - cr: required int, range: -3 to 30

### Traps
- random_trap(cr, dam_type)
    - cr: required int, range: -3 to 30
    - dam_type: optional str, range: ['bludgeoning', 'falling', 'piercing', 'slashing', 'poison', 'acid', 'fire', 'lightning', 'cold', 'necrotic']

### NPCs
- Npc()
