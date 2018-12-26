from aocd import get_data

import re
task_regex = re.compile("(\d+)\n[^\d]*(\d+),(\d+)")

s = get_data(day=22,year=2018)

#first part
def calculate_region(x,y):
    if (x,y) in erosion_levels:
        return
    if (x,y) == (0,0) or (x,y) == (target_x,target_y):
        erosion_levels[(x,y)] = depth%20183
    elif y == 0:
        erosion_levels[(x,y)] = (x*16807+depth)%20183
    elif x == 0:
        erosion_levels[(x,y)] = (y*48271+depth)%20183
    else:
        if (x-1,y) not in erosion_levels:
            calculate_region(x-1,y)
        if (x,y-1) not in erosion_levels:
            calculate_region(x,y-1)
        erosion_levels[(x,y)] = (erosion_levels[(x-1,y)]*erosion_levels[(x,y-1)]+depth)%20183
    regions[(x,y)] = erosion_levels[(x,y)]%3

erosion_levels = {}
regions = {}
depth,target_x,target_y = map(int,task_regex.search(s).group(1,2,3))
summa = 0
for i in range(target_x+1):
    for j in range(target_y+1):
        calculate_region(i,j)
        summa += regions[(i,j)]
print(summa)

#second part
def good_tools(x,y):
    if regions[(x,y)] == 0: return {1,2}
    elif regions[(x,y)] == 1: return {0,2}
    elif regions[(x,y)] == 2: return {0,1}

def neighbours(x,y):
    possibilities = filter(lambda p: p[0]>=0 and p[1]>=0, [(x-1,y),(x,y-1),(x,y+1),(x+1,y)])
    tools_here = good_tools(x,y)
    ns = []
    for p in possibilities:
        calculate_region(*p)
        tools_there = good_tools(*p)
        for t in tools_here & tools_there:
            ns.append((p[0],p[1],t))
    return ns

def strange_dijkstra(target_x,target_y):
    q = [(0,0,1)]
    dist = {(0,0,1): 0}
    target_dist = None
    while q:
        x,y,tool = q.pop(0)
        for a,b,t in neighbours(x,y):
            d = dist[(x,y,tool)] + 1 + 7*(t != tool)
            if target_dist is not None and d > target_dist:
                continue
            if (a,b,t) not in dist or dist[(a,b,t)] > d:
                dist[(a,b,t)] = d
                q.append((a,b,t))
                if (a,b,t) == (target_x,target_y,1):
                    target_dist = d
    return target_dist
print(strange_dijkstra(target_x,target_y))