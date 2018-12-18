from aocd import get_data

s = get_data(day=18,year=2018)

#first part
def apply_rule(t,surr):
    if t == ".":
        return "|" if surr.count("|")>=3 else "."
    elif t == "|":
        return "#" if surr.count("#") >= 3 else "|"
    elif t == "#":
        return "#" if "#" in surr and "|" in surr else "."
def is_in_map(game_map,x,y):
    return x>=0 and y>=0 and x<len(game_map) and y<len(game_map[0])
def neighbours(game_map,x,y):
    return [(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2) if (i!=x or j!=y) and is_in_map(game_map,i,j)]
def turn(game_map):
    new_game_map = []
    for x in range(len(game_map)):
        new_game_map_line = []
        for y in range(len(game_map[0])):
            surroundings = map(lambda p: game_map[p[0]][p[1]], neighbours(game_map,x,y))
            new_game_map_line.append(apply_rule(game_map[x][y],surroundings))
        new_game_map.append(new_game_map_line)
    return new_game_map
def print_map(game_map):
    print("\n".join(map("".join,game_map)))
    print()

def calculate_result(game_map):
    ts = sum(line.count("|") for line in game_map)
    ls = sum(line.count("#") for line in game_map)
    return (ts,ls,ts*ls)

game_map = map(list,s.split("\n"))
print_map(game_map)
for k in range(10):
    game_map = turn(game_map)
    print_map(game_map)
print(calculate_result(game_map))

#second part
game_map = map(list,s.split("\n"))
log = {}
k = 0
while True:
    tuple_party = tuple(map(tuple,game_map))
    if tuple_party in log:
        first_repeating = log[tuple_party]
        cycle_length = k-log[tuple_party]
        break
    log[tuple_party] = k
    log[k] = tuple_party
    game_map = turn(game_map)
    k += 1

time_passed = 1000000000
current_state = log[first_repeating + (time_passed - first_repeating)%cycle_length]
print(calculate_result(current_state))