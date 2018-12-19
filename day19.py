from aocd import get_data

s = get_data(day=19,year=2018)

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
    current_instr = instructions[register[ip]].split(" ")
    params = map(int,current_instr[1:]) + [register]
    locals()[current_instr[0]](*params)
    register[ip] += 1
print(register[0])

#second part
#result is sum of divisors of third register

ip = int(ip_setter[4])
register = [1] + [0]*5
while register[ip] != 1:
    current_instr = instructions[register[ip]].split(" ")
    params = map(int,current_instr[1:]) + [register]
    locals()[current_instr[0]](*params)
    register[ip] += 1

other_num = register[3]
summa = 0
for i in range(1,other_num+1):
    if other_num%i == 0:
        summa += i
print(summa)