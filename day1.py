#first part
s = """+1
-2
+3
+1"""

print(sum(map(int,s.split("\n"))))

#second part
*s, = map(int,"+3, +3, +4, -2, -4".split(", "))
reached = set()
f = 0
i = 0
while f not in reached:
  reached.add(f)
  f += s[i]
  i+=1
  i%=len(s)

print(f)