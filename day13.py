from aocd import get_data

s = get_data(day=13,year=2018)

#first part
class Cart:
    directions = "^>v<"
    def __init__(self,arrow,x,y):
        self.direction = arrow
        self.position = (x,y)
        self.intersection_num = 0
    def step(self,game_map):
        last_position = self.position
        
        self.go_to_neighbour_field(*last_position)  
        next_field = game_map[self.position]
        from_side = next_field.is_from_side(last_position)

        if next_field.type in "|-":
            pass
        elif next_field.type == "+":
            fun = [Cart.take_left_turn,Cart.dont_turn,Cart.take_right_turn][self.intersection_num]
            fun(self)
            self.intersection_num = (self.intersection_num + 1) % 3
        elif (next_field.type == "\\" and from_side) or (next_field.type == "/" and not from_side):
            self.take_right_turn()
        else:
            self.take_left_turn()
    def take_left_turn(self):
        self.direction = Cart.directions[(Cart.directions.index(self.direction)-1+len(Cart.directions))%len(Cart.directions)]
    def take_right_turn(self):
        self.direction = Cart.directions[(Cart.directions.index(self.direction)+1)%len(Cart.directions)]
    def dont_turn(self):
        pass
    def go_to_neighbour_field(self,x,y):
        self.position = [(x-1,y),(x,y+1),(x+1,y),(x,y-1)][Cart.directions.index(self.direction)]

class Path:
    def __init__(self,c,x,y):
        self.type = c
        self.position = (x,y)
    def is_from_side(self,last_position):
        return last_position[0] == self.position[0]

def parse_input(inp):
    inp = inp.split("\n")
    game_map = {}
    carts = []
    cart_positions = {}

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            c = inp[i][j]
            if c in "-><":
                game_map[(i,j)] = Path("-",i,j)
            elif c in "|^v":
                game_map[(i,j)] = Path("|",i,j)
            elif c in "/\\+":
                game_map[(i,j)] = Path(c,i,j)

            if c in "><^v":
                carts.append(Cart(c,i,j))
                cart_positions[(i,j)] = carts[-1]
    return game_map,carts,cart_positions
 
def play_turn(game_map,carts,cart_positions):
    collisions = []
    carts = sorted(carts,key=lambda c: c.position)
    broken = set()
    for c in carts:
        if c in broken: continue
        current_pos = c.position
        del cart_positions[current_pos]

        c.step(game_map)
        new_pos = c.position
        if new_pos in cart_positions:
            collisions.append(new_pos)
            broken.add(c)
            broken.add(cart_positions[new_pos])
            del cart_positions[new_pos]
        else:
            cart_positions[new_pos] = c
    for c in broken:
        carts.remove(c)
    return carts,collisions

def switch_coords(x,y):
    return y,x

game_map,carts,cart_positions = parse_input(s)
collisions = []
while not collisions:
    carts,collisions = play_turn(game_map,carts,cart_positions)
print(switch_coords(*collisions[0]))

#second part
while len(carts) > 1:
    carts,collisions = play_turn(game_map,carts,cart_positions)
print(switch_coords(*carts[0].position))