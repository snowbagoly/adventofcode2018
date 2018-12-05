from aocd import get_data

s = get_data(day=5,year=2018)

#first part
def shorten(polymer):
	leftPart = []
	rightPart = polymer
	while rightPart:
		if leftPart and leftPart[-1].upper() == rightPart[0].upper() and leftPart[-1].isupper() == rightPart[0].islower():
			leftPart.pop()
			rightPart.pop(0)
		else:
			leftPart.append(rightPart[0])
			rightPart.pop(0)
	return len(leftPart)
print(shorten(list(s)))

#second part
letters = set(s.lower())
s = list(s)
filtered_versions = [filter(lambda x: x.lower() != l, s) for l in letters]
print(min(map(shorten,filtered_versions)))