def monkey_banana_dfs(state, actions, path=[]):
    path = path + [state]
    if state == 'G':
        return path
    for action in actions[state]:
        next_state = action(state)
        if next_state not in path:
            new_path = monkey_banana_dfs(next_state, actions, path)
            if new_path:
                return new_path
    return None

def make_actions():
    def left(state):
        if state == 'L':
            return 'R'
        elif state == 'R':
            return 'L'
        return state

    def right(state):
        if state == 'L':
            return 'R'
        elif state == 'R':
            return 'L'
        return state

    def on_chair(state):
        if state == 'L' or state == 'R':
            return 'C'
        return state

    def off_chair(state):
        if state == 'C':
            return 'F'
        return state

    def grasp(state):
        if state == 'C':
            return 'G'
        return state

    actions = {
        'L': [on_chair, right],
        'R': [on_chair, left],
        'C': [off_chair, grasp],
        'F': [on_chair],
        'G': []
    }
    return actions

actions = make_actions()
initial_state = 'L'

result = monkey_banana_dfs(initial_state, actions)
if result:
    print("Solution path:", ' -> '.join(result))
else:
    print("No solution found.")
