from collections import deque

# Goal state
GOAL_STATE = [[1,2,3], [4,5,6], [7,8,0]]

# Moves: up, down, left, right
MOVES = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}

# Find position of tile in goal state
def goal_pos(tile):
    for i in range(3):
        for j in range(3):
            if GOAL_STATE[i][j] == tile:
                return (i,j)

# Compute Manhattan distance heuristic
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = goal_pos(tile)
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

# Convert state to tuple for hashing
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find blank tile position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i,j)

# BFS search
def bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))  # state and path
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        print("Current state:")
        for row in current_state:
            print(row)
        h = manhattan(current_state)
        print("Heuristic (Manhattan distance):", h)
        print("---")

        if current_state == GOAL_STATE:
            return path

        visited.add(state_to_tuple(current_state))

        blank_i, blank_j = find_blank(current_state)

        for move, (di, dj) in MOVES.items():
            new_i, new_j = blank_i + di, blank_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                # Create new state
                new_state = [row[:] for row in current_state]
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                state_tuple = state_to_tuple(new_state)
                if state_tuple not in visited:
                    queue.append((new_state, path + [move]))
    return None

if __name__ == "__main__":
    # Example initial state
    initial_state = [[1,2,3], [4,0,5], [7,8,6]]

    print("Initial State:")
    for row in initial_state:
        print(row)
    print("\nStarting BFS search...\n")

    solution = bfs(initial_state)

    if solution:
        print("\nOptimal solution path (sequence of moves):")
        print(solution)
        print("Number of moves:", len(solution))
    else:
        print("No solution found.")
