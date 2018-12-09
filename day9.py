from aocd import get_data

s = get_data(day=9,year=2018)

class Node:
    def __init__(self,value,previous,next):
        self.value = value
        self.next = next
        self.previous = previous
    def __repr__(self):
        return "value: %d" % self.value

#first part
s = s.split()
players = int(s[0])
n = int(s[6])

def calculate(last):
    zero = Node(0,None,None)
    one = Node(1,zero,zero)
    zero.next = one
    zero.previous = one
    current = one

    points = {i: 0 for i in range(players)}

    for i in range(2, last+1):
        if i%23 == 0:
            for j in range(7):
                current = current.previous
            before = current.previous
            after = current.next
            points[i%players] += i+current.value
            before.next = after
            after.previous = before
            del current
            current = after
        else:
            before = current.next
            after = before.next
            new_node = Node(i,before,after)
            before.next = new_node
            after.previous = new_node
            current = new_node

    maximum = max(points, key=points.get)
    return maximum, points[maximum]

print(calculate(n))
#second part
print(calculate(100*n))