from queue import PriorityQueue
import math
import Graph


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


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)

    search_queue.append((start_state, start_state.cost))
    if use_closed_list:
        closed_list[start_state] = True
    while len(search_queue) > 0:

        next_state = search_queue.pop()
        if goal_test(nextstate[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None:
                ptr = ptr.prev
                print(ptr)
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True
            search_queue.extend(successors)


## default heuristic - we can use this to implement uniform cost search
def h1(state):
    return 0


## you do this - return the straight-line distance between the state and (1,1)
def sld(state):
    return math.sqrt((state.g - 1) ** 2) + math.sqrt((state.h - 1) ** 2)


## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph.Graph()
    add_nodes(graph, filename)
    for nodes in graph.g:
        print(nodes)
    add_edges(graph, filename)
    for nodes in graph.g:
        print(nodes, graph.get_edges(nodes))

    return graph


def add_edges(graph, filename):
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            nodes = line.split(":")
            edges = nodes[1].split(" ")
            for edge in edges:
                if not edge == "":
                    newEdge = Graph.Edge(nodes[0], int(edge[0]), int(edge[2]))
                    graph.add_edge(newEdge)


def add_nodes(graph, filename):
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            nodes = line.split(":")
            graph.add_node(nodes[0])


if __name__ == "__main__":
    graph = read_mars_graph("marsmap")
