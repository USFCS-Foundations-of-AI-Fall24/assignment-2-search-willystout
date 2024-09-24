from queue import PriorityQueue
import math
from re import search

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

    def successors(self):
        edges = self.mars_graph.get_edges(self.location)
        return [(map_state(edge.dest, self.mars_graph, self, self.g + edge.val, 0), edge.val) for edge in
                edges]  # used autocomplete (I think GitHub coPilot)


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    curr_state = None
    # (f_value, state instance) ... in the minHeap
    search_queue.put((start_state.f, start_state))
    count = 0
    if use_closed_list:
        closed_list[start_state] = True
    while search_queue:
        # unpack cur_cost and next_state for each tuple in the queue
        cur_cost, curr_state = search_queue.get()
        successors = curr_state.successors()
        if goal_test(curr_state):
            print("Goal found")
            print(curr_state)
            ptr = curr_state
            while ptr is not None:
                ptr = ptr.prev_state
                print(ptr)
            print("A* count: ", count)
            return curr_state
        if use_closed_list:
            successors = [item for item in successors if item not in closed_list]
            for s in successors:
                closed_list[s] = True
            for successor, f_value in successors:
                count += 1
                new_state = map_state(location=successor.location, # create new state
                                      mars_graph=curr_state.mars_graph,
                                      prev_state=curr_state)
                new_state.g = curr_state.g + 1 # cost so far = curr_state.cost
                new_state.h = heuristic_fn(successor) # estimated cost to goal
                new_state.f = new_state.g + new_state.h # total estimated cost
                search_queue.put((new_state.f, new_state))


## default heuristic - we can use this to implement uniform cost search
def h1(state):
    return 0


## you do this - return the straight-line distance between the state and (1,1)
def sld(state):
    return math.sqrt((int(state.location[0]) - 1) ** 2) + math.sqrt((int(state.location[2]) - 1) ** 2)


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
            src = nodes[0]
            graph.add_node(src)
            dests = nodes[1].split(" ")[1:]
            for dest in dests:
                edge = Graph.Edge(src, dest, 0)
                graph.add_edge(edge)


def check_goal(state):
    return state.is_goal()


def test_route_finder():
    graph = read_mars_graph("marsmap")
    new_map_state = map_state("8,8", graph, None, 0, 0)
    print("A_STAR SEARCH WITH SLD")
    a_star_search = a_star(new_map_state, sld, check_goal, True)
    print("A_STAR SEARCH WITH H1")
    a_star_search_two = a_star(new_map_state, h1, check_goal, True)
