from aocd import get_data

import re
initial_regex = re.compile("([.#]+)")
rule_regex = re.compile("([.#]+) => ([.#]+)")

s = get_data(day=12,year=2018)
s = s.split("\n")

#first part
def create_rule(m):
    return m.group(1).replace("."," "),m.group(2).replace("."," ")
def step(state,fst_pot):
    state = " "*4 + state + " "*4
    new_state = ""
    for i in range(len(state)):
        new_state += rules.get(state[i-2:i+3], " ")
    fst_pot = fst_pot-4+new_state.find("#")
    return new_state.strip(),fst_pot

state = initial_regex.search(s[0]).group(1).replace(".", " ")
fst_pot = 0
rules = dict(map(create_rule,(rule_regex.match(line) for line in s[2:])))
for i in range(20):
    state,fst_pot = step(state,fst_pot)

print(sum(i+fst_pot for i in range(len(state)) if state[i] == "#"))

#second part
last_changing_state = state
last_turn = 20
while True:
    state,fst_pot = step(state,fst_pot)
    if state == last_changing_state:
        break
    last_changing_state = state
    last_turn += 1

k = 50000000000L-1
print(sum(i+fst_pot+(k-last_turn) for i in range(len(last_changing_state)) if last_changing_state[i] == "#"))