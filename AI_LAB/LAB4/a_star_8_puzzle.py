def h(move, target):
    # manhattan distance heuristic
    dist = 0
    for i in move:
        # store position of same value in state and goal state
        d1, d2 = move.index(i), target.index(i)
        x1, y1 = d1 % 3, d1 // 3
        x2, y2 = d2 % 3, d2 // 3
        # we calculate total manhattan of all the elements
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist


def gen(state, dir, b):
    # creating a copy of current state to modify
    state_copy = state.copy()
    if dir == 'l':
        state_copy[b - 1], state_copy[b] = state_copy[b], state_copy[b - 1]
    if dir == 'r':
        state_copy[b + 1], state_copy[b] = state_copy[b], state_copy[b + 1]
    if dir == 'u':
        state_copy[b - 3], state_copy[b] = state_copy[b], state_copy[b - 3]
    if dir == 'd':
        state_copy[b + 3], state_copy[b] = state_copy[b], state_copy[b + 3]
    return state_copy


def poss_moves(state, visited):
    b = state.index(-1)
    d = []
    if b not in [0, 1, 2]:
        d.append('u')
    if b not in [6, 7, 8]:
        d.append('d')
    if b not in [0, 3, 6]:
        d.append('l')
    if b not in [2, 5, 8]:
        d.append('r')
    final_moves = []
    for dir in d:
        final_moves.append(gen(state, dir, b))

    return [move for move in final_moves if move not in visited]


def print_grid(src):
    # create copy of state before printing to avoid changing -1 to blank in original which will give an error
    state = src.copy()
    state[state.index(-1)] = " "
    print("{} {} {}".format(state[0], state[1], state[2]))
    print("{} {} {}".format(state[3], state[4], state[5]))
    print("{} {} {}".format(state[6], state[7], state[8]))
    print("\n")
    return


def a_star(src, target):
    g = 0  # g is the level
    states = []
    states.append(src)
    visited = []
    while len(states):
        print("LEVEL {}".format(g))
        possible_moves = []
        for state in states:

            visited.append(state)
            print_grid(state)
            if state == target:
                print("Success")
                return

            possible_moves += [move for move in poss_moves(
                state, visited) if move not in possible_moves]
        print(possible_moves)
        cost = [g + h(move, target) for move in possible_moves]
        states = [possible_moves[i]
                  for i in range(len(possible_moves)) if cost[i] == min(cost)]
        g = g + 1
        if g > 3:
            print("NO SOLUTION")
            break


src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 6, 4, 5, -1, 7, 8]

a_star(src, target)
