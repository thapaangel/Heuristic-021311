import random

GOAL_STATE = ['A', 'B', 'C', 'D']

# Heuristic: number of blocks out of place
def heuristic(state):
    return sum(1 for i in range(4) if state[i] != GOAL_STATE[i])

# Generate neighbors by swapping adjacent blocks
def get_neighbors(state):
    neighbors = []
    for i in range(len(state)-1):
        new_state = state[:]
        new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
        neighbors.append((new_state, i))
    return neighbors

# Hill Climbing algorithm
def hill_climbing(initial_state):
    current_state = initial_state
    path = []

    print("Initial stack:", current_state)
    print("Heuristic:", heuristic(current_state))

    while True:
        neighbors = get_neighbors(current_state)
        neighbor_scores = [(heuristic(state), state, move_idx) for state, move_idx in neighbors]

        for score, state, _ in neighbor_scores:
            print("Neighbor state:", state, "Heuristic:", score)

        best_score, best_state, best_move = min(neighbor_scores, key=lambda x: x[0])

        if best_score < heuristic(current_state):
            path.append(f"Swap positions {best_move} and {best_move+1}")
            current_state = best_state
        else:
            break

        print("Move to:", current_state, "Heuristic:", best_score)

        if best_state == GOAL_STATE:
            break

    if current_state == GOAL_STATE:
        print("\nReached goal state!")
    else:
        print("\nAlgorithm got stuck in local optimum.")

    return path

if __name__ == "__main__":
    initial_stack = ['C', 'A', 'D', 'B']
    solution = hill_climbing(initial_stack)

    print("\nSolution path:")
    for step in solution:
        print(step)
