from aocd import get_data

s = get_data(day=8,year=2018)

class Node:
    def __init__(self, childNodes, metadata):
        self.children = childNodes
        self.metadata = metadata

    def metadata_sum(self):
        return sum(map(Node.metadata_sum,self.children))+sum(self.metadata)

    def get_value(self):
        if len(self.children) == 0: return self.metadata_sum()
        value = 0
        for m in self.metadata:
            if m-1 < len(self.children):
                value += self.children[m-1].get_value()
        return value

    def __repr__(self):
        return "Metadata: %s, children: [%s]" % (self.metadata, self.children)

#first part
def parse_tree(part):
    if part == []: return None
    number_of_children = part[0]
    number_of_metadata = part[1]
    if number_of_children == 0:
        return Node([],part[2:2+number_of_metadata]), part[2+number_of_metadata:]

    children = []
    remaining_part = part[2:]
    while len(children) < number_of_children:
        child,remaining_part = parse_tree(remaining_part)
        children.append(child)

    if number_of_metadata > 0:
        return Node(children, remaining_part[:number_of_metadata]), remaining_part[number_of_metadata:]
    else:
        return Node(children,[]), remaining_part

root = parse_tree(map(int,s.split()))[0]
print(root.metadata_sum())

#second part
print(root.get_value())