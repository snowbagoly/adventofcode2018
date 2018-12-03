from aocd import get_data

s = get_data(day=3,year=2018)

#first part
claims = s.split("\n")
reserved = set()
very_reserved = set()
for c in claims:
	id,data = c.split("@")
	x,y,w,h = map(int,data.strip().replace(",", " ").replace(": ", " ").replace("x", " ").split(" "))
	for i in range(x,x+w):
		for j in range(y,y+h):
			if (i,j) in reserved:
				very_reserved.add((i,j))
			else:
				reserved.add((i,j))

print(len(very_reserved))

#second part
overlapped = set()
ids = set()
reserved_by = {}
for c in claims:
	id,data = c.split("@")
	ids.add(id)
	x,y,w,h = map(int,data.strip().replace(",", " ").replace(": ", " ").replace("x", " ").split(" "))
	for i in range(x,x+w):
		for j in range(y,y+h):
			if (i,j) in reserved_by:
				overlapped.add(reserved_by[(i,j)])
				overlapped.add(id)
			else:
				reserved_by[(i,j)] = id
print(ids-overlapped)