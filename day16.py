from aocd import get_data

import re
registers_regex = re.compile("\[(\d+), (\d+), (\d+), (\d+)\]")

s = get_data(day=16,year=2018)

#first part
def addr(a,b,c,register):
    register[c] = register[a]+register[b]
    return register
def addi(a,b,c,register):
    register[c] = register[a]+b
    return register

def mulr(a,b,c,register):
    register[c] = register[a]*register[b]
    return register
def muli(a,b,c,register):
    register[c] = register[a]*b
    return register


def banr(a,b,c,register):
    register[c] = register[a]&register[b]
    return register
def bani(a,b,c,register):
    register[c] = register[a]&b
    return register


def borr(a,b,c,register):
    register[c] = register[a]|register[b]
    return register
def bori(a,b,c,register):
    register[c] = register[a]|b
    return register


def setr(a,b,c,register):
    register[c] = register[a]
    return register
def seti(a,b,c,register):
    register[c] = a
    return register


def gtir(a,b,c,register):
    register[c] = int(a>register[b])
    return register
def gtri(a,b,c,register):
    register[c] = int(register[a]>b)
    return register
def gtrr(a,b,c,register):
    register[c] = int(register[a]>register[b])
    return register


def eqir(a,b,c,register):
    register[c] = int(a == register[b])
    return register
def eqri(a,b,c,register):
    register[c] = int(register[a] == b)
    return register
def eqrr(a,b,c,register):
    register[c] = int(register[a] == register[b])
    return register

funs = {addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr}
fstpart,sndpart = s.split("\n"*4)

trials = fstpart.split("\n"*2)
counter = 0
possible = {}
for t in trials:
    before,instruction,after = t.split("\n")
    regsbefore = map(int,registers_regex.search(before).group(1,2,3,4))
    opcode,a,b,c = map(int,instruction.split())
    regsafter = map(int,registers_regex.search(after).group(1,2,3,4))
    possible_for_this = set()
    for f in funs:
        register = list(regsbefore) #copy
        try:
            if f(a,b,c,register) == regsafter:
                possible_for_this.add(f)
        except:
            pass
    if len(possible_for_this) >= 3:
        counter += 1
    #for part 2
    if opcode not in possible:
        possible[opcode] = possible_for_this
    else:
        possible[opcode] &= possible_for_this
print(counter)

#second part
instructions = {}
while len(possible) > 0:
    last = None
    for opcode in possible:
        if len(possible[opcode]) == 1:
            instructions[opcode] = possible[opcode].pop()
            del possible[opcode]
            last = instructions[opcode]
            break
    for opcode in possible:
        if last in possible[opcode]:
            possible[opcode].remove(last)

register = [0,0,0,0]
for line in sndpart.split("\n"):
    opcode,a,b,c = map(int,line.split())
    instructions[opcode](a,b,c,register)
print(register[0])