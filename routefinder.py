from queue import PriorityQueue
import math
import Graph
import mars_planner


class map_state:
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None, prev_state=None, g=0, h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == "1,1"

    def successors(self, state):
        edges = state.mars_graph.get_edges(state.location)
        return [(map_state(edge.dest, state.mars_graph, state, state.g + edge.val, 0), edge.val) for edge in edges] # used Autocomplete (I think GitHub coPilot)


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((start_state.g, start_state.h))
    count = 0
    if use_closed_list:
        closed_list[start_state] = True
    while search_queue.not_empty:
        next_state = search_queue.get()
        successors = next_state[0].successors(next_state)
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None:
                ptr = ptr.prev
                print(ptr)
            return next_state
        if use_closed_list:
            successors = [item for item in successors if item[0] not in closed_list]
            for s in successors:
                count += 1
                closed_list[s[0]] = True
        search_queue.put(successors)
    print("A* count: ", count)


## default heuristic - we can use this to implement uniform cost search
def h1(state):
    return 0


## you do this - return the straight-line distance between the state and (1,1)
def sld(state):
    return math.sqrt((state.location[0] - 1) ** 2) + math.sqrt((state.location[2] - 1) ** 2)


## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph.Graph()
    add_edges(graph, filename)
    return graph
    # CREATE A NEW MAP_STATE FOR EACH NODE OBJECT
    # a_star = start_state, heuristic_fn, goal_test, use_closed_list=True



def add_edges(graph, filename):
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            nodes = line.split(":")
            edges = nodes[1].split(" ")
            for edge in edges:
                if not edge == "":
                    # instead of the graph class we should use the map_state class
                    map_state = map_state(nodes[0], graph, None, int(edge[0]), int(edge[2]))
                    newEdge = Graph.Edge(nodes[0], int(edge[0]), int(edge[2]))
                    graph.add_edge(newEdge)


if __name__ == "__main__":
    read_mars_graph("marsmap")

    