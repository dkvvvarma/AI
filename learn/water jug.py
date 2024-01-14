def water_jug_dfs(x, y, target):
    def pour(state, action):
        if action == "fill_x":
            return (x, state[1])
        elif action == "fill_y":
            return (state[0], y)
        elif action == "empty_x":
            return (0, state[1])
        elif action == "empty_y":
            return (state[0], 0)
        elif action == "pour_x_y":
            poured = min(state[0], y - state[1])
            return (state[0] - poured, state[1] + poured)
        elif action == "pour_y_x":
            poured = min(state[1], x - state[0])
            return (state[0] + poured, state[1] - poured)

    def dfs(state, path=[]):
        path = path + [state]

        if state[0] == target or state[1] == target:
            return path

        for action in actions:
            next_state = pour(state, action)
            if next_state not in path:
                new_path = dfs(next_state, path)
                if new_path:
                    return new_path

        return None

    actions = ["fill_x", "fill_y", "empty_x", "empty_y", "pour_x_y", "pour_y_x"]

    initial_state = (0, 0)

    result = dfs(initial_state)

    return result

x_capacity = 4  # Capacity of jug X
y_capacity = 3  # Capacity of jug Y

target_amount = 2  # Target amount of water to measure

solution_path = water_jug_dfs(x_capacity, y_capacity, target_amount)

if solution_path:
    print("Solution path:")
    for state in solution_path:
        print(f"Jug X: {state[0]} liters, Jug Y: {state[1]} liters")
else:
    print("No solution found.")
