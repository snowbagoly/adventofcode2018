from aocd import get_data

import re
coord_regex = re.compile("(-?\d+),(-?\d+),(-?\d+),(-?\d+)")

s = get_data(day=25,year=2018)

def calculate_distance(p1,p2):
    return sum(map(lambda a,b: abs(a-b),p1,p2))

points = map(lambda line: map(int,coord_regex.search(line).group(1,2,3,4)),s.split("\n"))

edges = {i:[] for i in range(len(points))}
for i in range(len(points)-1):
    for j in range(i+1,len(points)):
        if calculate_distance(points[i],points[j]) <= 3:
            edges[i].append(j)
            edges[j].append(i)

points_left = set(range(len(points)))
counter = 0
while points_left:
    counter += 1
    q = [next(iter(points_left))]
    points_left.remove(q[0])
    while q:
        p = q.pop(0)
        for n in edges[p]:
            if n in points_left:
                q.append(n)
                points_left.remove(n)
print(counter)