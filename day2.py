from aocd import get_data

s = get_data(day=2,year=2018)

#first part
boxes = s.split("\n")
from collections import Counter
twoCounter = 0
threeCounter = 0
for box in boxes:
	letterCounts = Counter(box)
	containsTwo = any(letterCounts[letter] == 2 for letter in letterCounts)
	containsThree = any(letterCounts[letter] == 3 for letter in letterCounts)
	if containsTwo: twoCounter += 1
	if containsThree: threeCounter += 1
print(twoCounter, threeCounter, twoCounter*threeCounter)

#second part
def find_similars(boxes):
	for i in range(len(boxes)):
		for j in range(i+1,len(boxes)):
			d,similarPart = diff(boxes[i],boxes[j])
			if d == 1: return boxes[i],boxes[j],d,similarPart

def diff(a,b):
	similars = ""
	difference = 0
	for k in range(len(a)):
		if a[k] == b[k]:
			similars += a[k]
		else:
			difference += 1
			if difference > 1: break
	return difference, similars

print(find_similars(boxes))