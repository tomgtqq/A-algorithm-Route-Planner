import math

DEBUG = False


def shortest_path(M, start, goal):
    print("shortest path called")

    if start not in M.intersections or goal not in M.intersections:
        print("Please check input")
        return None

    explored = set()
    curr_state = start
    # Data struct is { node in frontier: [[ s0, s1, s2, s3, s4...], g value ,h value, f value]}
    paths = {start: [[start], 0, 0, 0]}

    while not goal_test(paths, goal):

        for state in M.roads[curr_state]:
            # check the state , if it's explored then continue next state
            if state in explored:
                continue

            curr_path = dict()
            curr_path[state] = [[], 0, 0, 0]
            curr_path[state][0].extend(paths[curr_state][0])
            curr_path[state][0].append(state)
            curr_path[state][1:] = paths[curr_state][1:]

            # Calculate g value  + the original g value (path cost)
            curr_path[state][1] += calculate_g_value(M, state, curr_state)
            # Calculate h value
            curr_path[state][2] = calculate_h_value(M, state, goal)
            # Calculate f value
            curr_path[state][3] = calculate_f_value(curr_path, state)

            if state in paths.keys():
                if curr_path[state][3] < paths[state][3]:
                    paths[state] = curr_path[state]
            else:
                paths[state] = curr_path[state]

        del paths[curr_state]

        explored.add(curr_state)
        curr_state = min((values[3], state)
                         for state, values in paths.items())[1]

        if DEBUG:
            print(f'shortest_path() << curr_state << {curr_state}')

        if not paths:
            return None

    return paths[curr_state][0]


def goal_test(paths, goal):
    cheapest_state = list(paths.keys())[0]
    cheapest_f_value = math.inf

    if DEBUG:
        print(f'goal_test() << list(paths.keys()) << {list(paths.keys())}')

    for node, values in paths.items():
        if values[3] < cheapest_f_value:
            cheapest_f_value = values[3]
            cheapest_state = node

    if cheapest_state == goal:
        return True

    return False


def calculate_g_value(M, state, curr_state):
    # path cost from current state to a candidate state
    path_cost = math.sqrt(math.pow(M.intersections[state][0] - M.intersections[curr_state][0], 2) +
                          math.pow(M.intersections[state][1] - M.intersections[curr_state][1], 2))
    return path_cost


def calculate_h_value(M, state, goal):
    # heristic value from a candidate state to the goal
    est_distance = math.sqrt(math.pow(M.intersections[state][0] - M.intersections[goal][0], 2) +
                             math.pow(M.intersections[state][1] - M.intersections[goal][1], 2))
    return est_distance


def calculate_f_value(curr_path, state):
    # f = g + h
    total_cost = curr_path[state][1] + curr_path[state][2]
    return total_cost
