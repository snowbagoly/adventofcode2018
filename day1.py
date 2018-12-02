from aocd import get_data

s = get_data(day=1,year=2018)

#first part
print(sum(map(int,s.split("\n"))))

#second part
s = list(map(int,s.split("\n")))
reached = set()
f = 0
i = 0
while f not in reached:
  reached.add(f)
  f += s[i]
  i+=1
  i%=len(s)

print(f)