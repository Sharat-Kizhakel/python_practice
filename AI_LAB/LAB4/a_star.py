import math

src = int(input("Enter the source x-coordinate:")
          ), int(input("Enter the source y-coordinate:"))
target = int(input("Enter the goal x-coordinate:")
             ), int(input("Enter the goal y-coordinates"))
print("source:")
print(src)
print("goal:")
print(target)
maze_row = []
maze = []
for i in range(4):
    print("enter row {}:".format(i + 1))
    for j in range(5):
        maze_row.append(
            int(input("Enter the maze coordinate [{}][{}]:".format(i, j))))
    maze.append(maze_row)
    maze_row = []

print(maze)


def possible_moves(pos, visited):
    pos_moves = []
    i, j = pos
    for l in [i - 1, i, i + 1]:
        for m in [j - 1, j, j + 1]:
            # initially val will be neg
            if l >= 0 and m >= 0 and l < len(maze) and m < len(maze[0]) and not ((l, m) == (i, j)) and maze[l][m] != 1:
                if (l, m) not in visited:
                    pos_moves.append((l, m))
    return pos_moves


def h(pos1, pos2):  # heuristic h(n)
    x1, y1 = pos1
    x2, y2 = pos2
    dist = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    return dist


def a_star(src, target, visited, d):
    visited.append(src)
    if(src == target):
        return visited
    pos_moves = possible_moves(src, visited)
    if (pos_moves == []):
        return False
    # calculating f(n) values
    scores = [h(x, target) + d for x in pos_moves]
    min_score = min(scores)  # take the lowest cost score
    selected_moves = []
    for i in range(len(pos_moves)):
        if scores[i] == min_score:
            # adding lowest cost move
            selected_moves.append(pos_moves[i])
    for move in selected_moves:
        # dist has to be increased and new source is move
        if a_star(move, target, visited, d + 1) != False:
            return visited
    return False


def solve_maze(source, target):
    visited = []
    # 4th param is distance from the source basically g(n) dist is 0 from itself
    res = a_star(source, target, visited, 0)
    if not res:
        print("No path exists")
    else:
        print("Path exists", res)
        display(res)


def display(valid_moves):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in valid_moves:
                print("#", end=' ')  # the poss path will be with '#'
            else:
                print(maze[i][j], end=' ')
        print()
    print()


solve_maze(src, target)

# src=0,0
# target=3,3
# maze=[[0,1,0,0,1],[1,0,0,1,1],[1,0,1,0,1],[1,1,1,0,1]]
