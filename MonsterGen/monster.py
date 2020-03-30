import itertools
from Fortuna import distribution_range, middle_linear
from MonsterGen.monster_lib import monster_stats, CR, random_monster


class Monster:

    def __init__(self, cr):
        self.Name = random_monster()
        self.CR = CR(cr)
        hp_range = monster_stats["HP Range"][self.CR.key]
        self.HP = distribution_range(middle_linear, *hp_range)
        self.AC = monster_stats["AC"][self.CR.key]
        self.ATT = monster_stats["ATT"][self.CR.key]
        self.DC = monster_stats["DC"][self.CR.key]
        damage_range = monster_stats["Damage Range"][self.CR.key]
        self.Damage = distribution_range(middle_linear, *damage_range)
        self.XP = monster_stats["XP"][self.CR.key]

    def __str__(self):
        output = (f"{k}: {v}" for k, v in self.__dict__.items())
        return '\n'.join(itertools.chain(output, ("",)))


if __name__ == '__main__':

    print(Monster(10))
