from collections import OrderedDict
import heapq
import math

DEBUG = True


class PriorityQueque:
    def __init__(self):
        self._queque = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queque, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queque)


def shortest_path(M, start, goal):
    print("shortest path called")

    unexplored = set(M.intersections.keys())
    explored = set()

    if not start in unexplored or not goal in unexplored:
        print("Please check input")
        return

    path_cost = 0
    total_cost = h(start, goal, M)

    # Push path to OrderedDict to save the paths, the key is state and value is a net dict contains path_cost
    path = OrderedDict({start: {"state": start, "path_cost": path_cost}})

    frontier = PriorityQueque()
    frontier.push(path, total_cost)

    unexplored.remove(start)

    if DEBUG_unexplored_explored_frontier:
        print(f'unexplored {unexplored}')
        print(f'explored {explored}')
        pprint.pprint(frontier)

    while len(unexplored):
        path = frontier.pop()[2]

        if DEBUG:
            print(f'path {path}')

        curr = path[next(reversed(path))]

        if DEBUG:
            print(f'curr {curr}')

        if curr["state"] is goal:
            return list(path.keys())

        if DEBUG:
            print(f'curr["state"] {curr["state"]}')
            print(f'M.roads[curr["state"]] {M.roads[curr["state"]]}')

        for state in M.roads[curr["state"]]:
            if not state in explored:
                path_cost = curr["path_cost"] + g(curr["state"], state, M)
                total_cost = path_cost + h(state, goal, M)
                # update the path
                path.update({state: {"state": state, "path_cost": path_cost}})
                # Push state into frontier
                frontier.push(path, total_cost)

        explored.add(curr["state"])
        # Remove state from unexplored
        unexplored.remove(curr["state"])

        if DEBUG_unexplored_explored_frontier:
            print(f'unexplored {unexplored}')
            print(f'explored {explored}')
            pprint.pprint(frontier)


def g(s1, s2, M):

    s1_coordinate = M.intersections[s1]
    s2_coordinate = M.intersections[s2]

    # Step path cost
    x = s2_coordinate[0] - s1_coordinate[0]
    y = s2_coordinate[1] - s1_coordinate[1]

    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def h(s, goal, M):
    s_coordinate = M.intersections[s]
    g_coordinate = M.intersections[goal]

    # Est Distance
    x = g_coordinate[0] - s_coordinate[0]
    y = g_coordinate[1] - s_coordinate[1]

    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
