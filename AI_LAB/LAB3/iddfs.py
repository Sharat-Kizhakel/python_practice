# LAB3 Implement Iterative deepening search algorithm.

def dfs(src, target, maxDepth, visited_states):
    if src == target:
        return True
    if maxDepth <= 0:
        return False
    visited_states.append(src)
    moves = possible_moves(src, visited_states)
    for move in moves:
        if dfs(move, target, maxDepth - 1, visited_states):
            return True
    return False


def gen(src, b, dir):
    state = src.copy()
    if dir == 'd':
        state[b + 3], state[b] = state[b], state[b + 3]
    if dir == 'u':
        state[b - 3], state[b] = state[b], state[b - 3]
    if dir == 'l':
        state[b - 1], state[b] = state[b], state[b - 1]
    if dir == 'r':
        state[b + 1], state[b] = state[b], state[b + 1]
    return state


def possible_moves(src, visited_states):

    d = []
    b = src.index(-1)
    if b not in [0, 1, 2]:
        d.append('u')
    if b not in [6, 7, 8]:
        d.append('d')
    if b not in [0, 3, 6]:
        d.append('l')
    if b not in [2, 5, 8]:
        d.append('r')
    temp = []
    for dir in d:
        temp.append(gen(src, b, dir))
    return [moves for moves in temp if moves not in visited_states]


def iddfs(src, goal, depth):
    for i in range(depth):
        visited_states = []
        if dfs(src, goal, i + 1, visited_states):
            return True
    return False


src = []
goal = []
print("enter the values 1 to 8 and -1 for blank space")
for i in range(9):
    src.append(int(input("Index {}:".format(i))))
print("source")
print(src)
for i in range(9):
    goal.append(int(input("Index {}:".format(i))))
print("goal")
print(goal)
depth = int(input("Enter the max depth:"))
print(20 * "*")

print(iddfs(src, goal, depth))

# src = [1,2,3,-1,4,5,6,7,8]
# target = [1,2,3,4,5,-1,6,7,8]
