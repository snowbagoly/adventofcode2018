from aocd import get_data
import copy
import re
line_regex = re.compile("(\\d+) units each with (\\d+) hit points(.+)with an attack that does (\\d+) (\\S+) damage at initiative (\\d+)")

s = get_data(day=24,year=2018)

class Group:
    def __init__(self,**kwargs):
        self.data = kwargs
        self.target = None
    @property
    def effective_power(self):
        return self.data["units"]*self.data["dmg"]
    def __repr__(self):
        return "<Group %s>" % self.data
    def calculate_attack_power(self, t):
        if self.data["dmg_type"] in t.data["immune_to"] or (self.type == t.type):
            multiplier = 0
        elif self.data["dmg_type"] in t.data["weak_to"]:
            multiplier = 2
        else:
            multiplier = 1
        return multiplier * self.effective_power
    def target_chooser(self, t):
        return self.calculate_attack_power(t), t.effective_power, t.data["initiative"]
    def kill_units(self):
        if self.data["units"] <= 0 or self.target == None: return False

        damage = self.calculate_attack_power(self.target)
        was_effective = self.target.lose_units(damage)
        self.target = None
        return was_effective
    def lose_units(self, damage):
        dead = damage//self.data["hp"]
        self.data["units"] -= dead
        return dead > 0


def parse_line(line):
    units,hp,spec,dmg,dmg_type,initiative = line_regex.match(line).group(*range(1,7))
    units,hp,dmg,initiative = map(int,(units,hp,dmg,initiative))
    weak_to = immune_to = ""
    spec = spec.split(";")
    for s in spec:
        if "weak" in s:
            weak_to = s
        elif "immune" in s:
            immune_to = s
    return Group(units=units, hp=hp, weak_to=weak_to, immune_to=immune_to, dmg=dmg, dmg_type=dmg_type, initiative=initiative)
    

def select_targets(groups):
    groups = sorted(groups, key=lambda g: (g.effective_power,g.data["initiative"]), reverse=True)
    possible_targets = set(groups)
    for g in groups:
        target = max(possible_targets, key=g.target_chooser)
        if g.target_chooser(target)[0] <= 0: continue #if cannot deal damage, then not choose target
        g.target = target
        possible_targets.remove(target)
    return groups

def attack(groups):
    groups = sorted(groups, key=lambda g: g.data["initiative"], reverse=True)
    effect = 0
    for g in groups:
        effect += g.kill_units()
    immune_groups = []
    infection_groups = []
    for g in groups:
        if g.data["units"] > 0:
            if g.type == 0:
                immune_groups.append(g)
            elif g.type == 1:
                infection_groups.append(g)
    return effect,immune_groups,infection_groups

def fight(immune_groups, infection_groups):
    effect = 1
    while len(immune_groups) * len(infection_groups) * effect > 0:
        groups = select_targets(immune_groups + infection_groups)    
        effect,immune_groups,infection_groups = attack(groups)
    return immune_groups,infection_groups

immune_s,infection_s = s.split("\n\n")
original_immune_groups = list(map(parse_line,immune_s.split("\n")[1:]))
for g in original_immune_groups: g.type = 0; g.id = original_immune_groups.index(g)+1
original_infection_groups = list(map(parse_line,infection_s.split("\n")[1:]))
for g in original_infection_groups: g.type = 1; g.id = original_infection_groups.index(g)+1

immune_groups,infection_groups = fight(copy.deepcopy(original_immune_groups),copy.deepcopy(original_infection_groups))
print(sum(g.data["units"] for g in immune_groups + infection_groups))

#second part
def boost(immune_groups,infection_groups,b):
    for g in immune_groups:
        g.data["dmg"] += b
    immune_groups,infection_groups = fight(immune_groups,infection_groups)
    if len(immune_groups) > 0 and len(infection_groups) == 0:
        return immune_groups
    else: return None

win_result = None
b = 0
while win_result is None:
    b += 1
    win_result = boost(copy.deepcopy(original_immune_groups),copy.deepcopy(original_infection_groups),b)
print(b,sum(g.data["units"] for g in win_result))