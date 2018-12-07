from aocd import get_data

s = get_data(day=7,year=2018)

#first part
def req(line):
    return line[5]
def cons(line):
    return line[36]

preconditions = {}
precondition_for = {}
letters = set()
for line in s.split("\n"):
    r,c = req(line),cons(line)
    if c not in preconditions:
        preconditions[c] = set()
    if r not in precondition_for:
        precondition_for[r] = set()
    preconditions[c].add(r)
    precondition_for[r].add(c)
    letters.add(r)
    letters.add(c)

letters = sorted(letters)
done = set()
order = ""
while letters:
    for i in range(len(letters)):
        l = letters[i]
        if l not in preconditions or not preconditions[l]-done:
            order += l
            done.add(l)
            del letters[i]
            break
print(order, len(order))

#second part
def time_for(letter):
    return 60+ord(letter)-ord('A')+1

letters = sorted(order)

number_of_workers = 5
in_progress = [] #the letters are in the order of finishing
worked_on = {i: set() for i in range(number_of_workers)}
ready_on = {}

current = 0
while len(in_progress) < len(letters):
    done = in_progress[:current]
    done_time = ready_on[done[-1]] if done else 0
    free_elves = [w for w in worked_on if not worked_on[w]-set(done)]
    assigned_now = 0
    for i in range(len(letters)):
        l = letters[i]
        if l in in_progress: continue

        if l not in preconditions or not preconditions[l]-set(done):
            my_elf = free_elves[assigned_now]
            assigned_now += 1
            worked_on[my_elf].add(l)
            ready_on[l] = done_time+time_for(l)
            j = 0
            while j<len(in_progress) and ready_on[in_progress[j]]<=ready_on[l]: j+=1
            in_progress.insert(j,l)
            if assigned_now == len(free_elves): break
    current += 1

maxready = 0
for l in ready_on:
    if ready_on[l] > maxready:
        maxready = ready_on[l]
print(maxready)