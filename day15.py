from aocd import get_data

s = get_data(day=15,year=2018)

#first part
def attack_value(type):
    global elf_attack_power
    return elf_attack_power if type == "E" else 3
def friend(type):
    return "E" if type == "E" else "G"
def enemy(type):
    return "G" if type == "E" else "E"
def neighbours(game_map,x,y):
    return filter(lambda pos: pos in game_map, [(x-1,y), (x,y-1), (x,y+1), (x+1,y)])
def first_in_reading_order(positions):
    return min(positions)
def find_target(game_map,x,y):
    type = game_map[(x,y)][0]
    q = [(x,y)]
    dist = {(x,y): 0}
    parent = {(x,y): None}
    nearest_enemy_distance = None
    nearest_enemy_positions= []
    while q:
        p = q.pop(0)
        dist_p = dist[p]
        if nearest_enemy_distance is not None and dist_p + 1 > nearest_enemy_distance:
            break
        for n in neighbours(game_map,*p):
            if game_map[n][0] == friend(type):
                continue
            if n not in dist:
                dist[n] = dist_p + 1
                parent[n] = p
                if game_map[n][0] == enemy(type):
                    nearest_enemy_distance = dist_p + 1
                    nearest_enemy_positions.append(n)
                else:
                    q.append(n)
    if nearest_enemy_positions:
        target = first_in_reading_order(nearest_enemy_positions)
        p = parent[target]
        while parent[p] != (x,y) and parent[p] != None: p = parent[p]
        return p
    else:
        return (x,y)
def attack(game_map,x,y):
    global number_of_elves,number_of_goblins
    targets = []
    type = game_map[(x,y)][0]
    for p in neighbours(game_map,x,y):
        if game_map[p][0] == enemy(type):
            targets.append((game_map[p][1],p))
    if targets:
        targets.sort()
        target_pos = targets[0][1]
        game_map[target_pos] = (game_map[target_pos][0],game_map[target_pos][1]-attack_value(type))
        if game_map[target_pos][1] <= 0:
            number_of_elves -= game_map[target_pos][0] == "E"
            number_of_goblins -= game_map[target_pos][0] == "G"
            game_map[target_pos] = (".",200)

def turn(game_map):
    players = sorted(pos for pos in game_map if game_map[pos][0] in "EG")
    for i in range(len(players)):
        p = players[i]
        if game_map[p][0] not in "EG": continue #if died earlier in this turn

        new_p = find_target(game_map,*p)
        game_map[p],game_map[new_p] = game_map[new_p],game_map[p]
        attack(game_map,*new_p)
        if number_of_elves*number_of_goblins == 0: #every enemy died
            #check if players left are dead enemies
            for j in range(i+1,len(players)):
                if game_map[p][0] in "EG":
                    return 0 #the turn was not finished
            break
    return 1 #the turn was properly finished


def parse_input(input):
    global width,height,number_of_elves,number_of_goblins
    s = input.split("\n")
    number_of_elves = number_of_goblins = 0
    game_map = {}
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] in ".EG":
                game_map[(i,j)] = (s[i][j],200)
                number_of_elves += s[i][j] == "E"
                number_of_goblins += s[i][j] == "G"
    width = len(s[0])
    height = len(s)
    return game_map

def print_map(game_map):
    global width,height
    for i in range(height):
        line = ""
        line_end = []
        for j in range(width):
            line += game_map.get((i,j),"#")[0]
            if (i,j) in game_map and game_map[(i,j)][0] in "EG":
                line_end.append("%s(%d)" % game_map[(i,j)])
        print(line + "   " + ", ".join(line_end))
    print()
def sum_hp(game_map):
    summa = 0
    for p in game_map:
        if game_map[p][0] in "EG":
            summa += game_map[p][1]
    return summa

game_map = parse_input(s)
elf_attack_power = 3
print_map(game_map)
k=0
while number_of_elves*number_of_goblins > 0:
    k+=turn(game_map)
    print_map(game_map)
summa = sum_hp(game_map)
print(k,summa,k*summa)

#second part
game_map = parse_input(s)
start_number_of_elves = number_of_elves
elf_attack_power = 4
k = 0
while number_of_goblins > 0:
    if number_of_elves < start_number_of_elves:
        game_map = parse_input(s)
        elf_attack_power += 1
        k = 0
    k+=turn(game_map)
summa = sum_hp(game_map)
print(elf_attack_power,k,summa,k*summa)