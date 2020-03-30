from Fortuna import distribution_range, middle_linear, plus_or_minus_linear
from MonsterGen.monster_lib import monster_stats, CR, random_monster, rank_by_tier


class Monster:

    def __init__(self, cr):
        self.cr = CR(cr) if type(cr) == int else cr
        self.tier = self.cr.tier
        self.rank = rank_by_tier(str(self.tier))
        self.name = random_monster(self.rank)
        self.variance = plus_or_minus_linear(3)
        self.hp_range = monster_stats["HP Range"][self.cr.key]
        self.hp = distribution_range(middle_linear, *self.hp_range)
        self.ac = monster_stats["AC"][self.cr.key] + self.variance
        self.att = monster_stats["ATT"][self.cr.key] - self.variance
        self.dc = monster_stats["DC"][self.cr.key]
        self.damage_range = monster_stats["Damage Range"][self.cr.key]
        self.damage = distribution_range(middle_linear, *self.damage_range)
        self.xp = monster_stats["XP"][self.cr.key]

    def to_dict(self):
        lo_dam, hi_dam = self.damage_range
        return {
            "Name": self.name,
            "CR": self.cr.string,
            "Hit Points": self.hp,
            "Armor Class": self.ac,
            "Attack Bonus": self.att,
            "Typical Damage": f"{lo_dam} - {hi_dam}",
            "Save DC": self.dc,
            "XP Value": self.xp,
        }

    def __str__(self):
        output = (f"{k}: {v}" for k, v in self.to_dict().items())
        return '\n'.join(output)


if __name__ == '__main__':
    monster_cr = CR.party_adapter(average_level=10, num_players=3, difficulty=0)
    print(Monster(monster_cr))
