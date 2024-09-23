from collections import deque


## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True):
    search_queue = deque()
    closed_list = {}
    count = 0

    search_queue.append((startState, ""))
    if use_closed_list:
        closed_list[startState] = True
    while len(search_queue) > 0:
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            # print("Goal found")
            ptr = next_state[0]
            while ptr is not None:
                ptr = ptr.prev
                # print(ptr)
            print("BFS count: ", count)
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors
                              if item[0] not in closed_list]
                for s in successors:
                    count += 1
                    closed_list[s[0]] = True
            search_queue.extend(successors)


### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True, limit=0):
    search_queue = deque()
    closed_list = {}
    count = 0

    search_queue.append((startState, ""))
    if use_closed_list:
        closed_list[startState] = True
    while len(search_queue) > 0:
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            # print("Goal found")
            ptr = next_state[0]
            while ptr is not None:
                ptr = ptr.prev
                # print(ptr)
            print("DFS count: ", count)
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors
                              if item[0] not in closed_list]
                for s in successors:
                    count += 1
                    closed_list[s[0]] = True
            search_queue.extend(successors)


## add iterative deepening search here

def depth_limited_search(startState, action_list, goal_test, limit, use_closed_list=True):
    search_queue = deque()
    closed_list = {}
    count = 0

    search_queue.append((startState, ""))
    if use_closed_list:
        closed_list[startState] = True
    while len(search_queue) > 0:
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            # print("Goal found")
            ptr = next_state[0]
            while ptr is not None:
                ptr = ptr.prev
                # print(ptr)
            print("DLS count: ", count)
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors
                              if item[0] not in closed_list]
                for s in successors:
                    if count >= limit:
                        break
                    count += 1
                    closed_list[s[0]] = True
            search_queue.extend(successors)
