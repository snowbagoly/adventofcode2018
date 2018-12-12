from aocd import get_data

import re
positions = re.compile("position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>")

s = get_data(day=10,year=2018)

#first part
class Star:
    def __init__(self,x,y,vx,vy):
        self.x, self.y, self.vx, self.vy = x,y,vx,vy
    def step(self):
        self.x += self.vx
        self.y += self.vy
    def step_back(self):
        self.x -= self.vx
        self.y -= self.vy
    def __repr__(self):
        return "<Star %d,%d,%d,%d>" % (self.x,self.y,self.vx,self.vy)

def print_sky(stars):
    min_x = min(s.x for s in stars)
    max_x = max(s.x for s in stars)
    min_y = min(s.y for s in stars)
    max_y = max(s.y for s in stars)
    sky = [[" " for i in range(min_x,max_x+1)] for j in range(min_y,max_y+1)]
    for s in stars:
        sky[s.y-min_y][s.x-min_x] = "#"
    for line in sky:
        print("".join(line))

stars = map(lambda m: Star(*[int(m.group(i+1)) for i in range(4)]), (positions.match(line) for line in s.split("\n")))

last_distance = 1000000
for i in range(100000):
    for s in stars: s.step()
    min_y = min(s.y for s in stars)
    max_y = max(s.y for s in stars)
    distance = max_y - min_y
    if distance > last_distance:
        for s in stars: s.step_back()
        print_sky(stars)
        print(i) #second part
        break
    last_distance = distance