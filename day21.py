from aocd import get_data

s = get_data(day=21,year=2018)

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

s = s.split("\n")
ip_setter,instructions = s[0],s[1:]

ip = int(ip_setter[4])
register = [0]*6
while register[ip] < len(instructions):
    if register[ip] == 25:
        register[2] = register[4]//256 # in my input the magic happens when register[2]*256 > register[4]
    if register[ip] == 29: # in my input in this instruction, register 0 is compared to register 5
        print(register[5])
        break
    current_instr = instructions[register[ip]].split(" ")
    params = map(int,current_instr[1:]) + [register]
    locals()[current_instr[0]](*params)
    register[ip] += 1

#second part
ip = int(ip_setter[4])
register = [0,0,0,0,0,0]
votma = set()
possible_halt_nums = list()
while register[ip] < len(instructions):
    if register[ip] == 29:  # in my input in this instruction, register 0 is compared to register 5
        if register[5] in votma:
            break
        votma.add(register[5])
        possible_halt_nums.append(register[5])
    if register[ip] == 25:
        register[2] = register[4]//256 # in my input the magic happens when register[2]*256 > register[4]
    current_instr = instructions[register[ip]].split(" ")
    params = map(int,current_instr[1:]) + [register]
    locals()[current_instr[0]](*params)
    register[ip] += 1

print(possible_halt_nums[-1])