from aocd import get_data

s = int(get_data(day=11,year=2018))

#first part
def cell(x,y):
    return (((x+10)*y + s)*(x+10))//100%10-5

def calculate_square(from_x,from_y,to_x,to_y,cells):
    return sum(cells[j][i] for i in range(from_x,to_x) for j in range(from_y,to_y))
def find_largest_nxn(cells,n):
    max_square = 0
    max_pos = None,None
    for i in range(1,len(cells)-n+1):
        for j in range(1,len(cells)-n+1):
            square = calculate_square(i,j,i+n,j+n,cells)
            if square > max_square:
                max_square = square
                max_pos = i,j
    return max_square,max_pos

cells = []
for i in range(301):
    row = []
    for j in range(301):
        row.append(cell(j,i))
    cells.append(row)
print(find_largest_nxn(cells,3))

#second part
max_square,max_pos,size = 0,(None,None),None
for n in range(3,21):
    sq,p = find_largest_nxn(cells,n)
    if sq > max_square:
        max_square = sq
        max_pos = p
        size = n
print(max_square,max_pos,size)