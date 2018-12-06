from aocd import get_data

s = get_data(day=6,year=2018)

#first part
def neighbours(x,y):
	return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
def is_border_point(p,lx,rx,ly,ry):
	return p[0] in (lx,rx) or p[1] in (ly,ry)
def bfs(starters,lx,rx,ly,ry):
	distances = { starter: (0,[starter]) for starter in starters}
	borders = lx,ry,ly,ry
	q = list(starters)
	infinite_points = set(starter for starter in starters if is_border_point(starter,*borders))
	while q:
		p = q.pop(0)
		dist_from = distances[p][1][0]
		dist_p = distances[p][0]
		for n in neighbours(*p):
			if lx<=n[0] and n[0]<=rx and ly<=n[1] and n[1]<=ry:
				was_reached = n in distances
				must_modify = not was_reached or \
				 (distances[n][0] >= dist_p + 1 and dist_from not in distances[n][1])
				if was_reached and must_modify:
					distances[n][1].append(dist_from)
				elif not was_reached and must_modify:
					distances[n] = (dist_p + 1,[dist_from])
					q.append(n)
					if dist_from not in infinite_points and is_border_point(n,*borders):
						infinite_points.add(dist_from)
	return distances, infinite_points

coords = list(map(lambda d: tuple(map(int,d.split(", "))), s.split("\n")))
xcoords,ycoords = map(lambda c: c[0], coords), map(lambda c: c[1], coords)
borders = min(xcoords),max(xcoords),min(ycoords),max(ycoords)
distances,infinite_points = bfs(coords,*borders)

counter = {coord : 0 for coord in coords}
for p in distances:
	if len(distances[p][1]) == 1:
		add_to = distances[p][1][0]
		if add_to not in infinite_points:
			counter[add_to] += 1
maximum = max(counter, key=counter.get)

print(maximum, counter[maximum])

#second part
def manhattan_dist(p1,p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

in_region = 0
threshold = 10000
for p in distances:
	summa = 0
	for c in coords:
		summa += manhattan_dist(p,c)
		if summa >= threshold:
			break
	else:
		in_region += 1
print(in_region)