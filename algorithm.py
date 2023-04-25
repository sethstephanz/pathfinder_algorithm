# This program uses a BFS approach to find the shortest path between two nodes in a graph, if a path exists.

def solve_puzzle(puzzle, starting_vertex, destination):
    """
    This function converts maze into a table, which is then filled out using a breadth-first search.
    If the destination is able to be reached from the starting vertex, the table is then fed to a function
    that returns the shortest path and the directions taken.
    """
    # if starting vertex is same as destination, return right away
    if starting_vertex == destination:
        return [starting_vertex]

    # create graphical representation of maze to fill out with bfs
    graph = []
    for row1 in puzzle:
        mapRow = []
        for element in row1:
            if element == '-':
                mapRow.append(0)
            else:
                mapRow.append('X')
        graph.append(mapRow)
    i = starting_vertex[0]
    pos = starting_vertex

    # initialize queue and go through first item manually
    queue = []

    rowlength = len(graph[0]) - 1
    columnheight = len(graph) - 1
    vert = pos[0]
    hor = pos[1]
    up = None
    down = None
    left = None
    right = None

    if vert == columnheight:  # we're at bottom of graph. nothing to add to bottom
        down = None
    else:
        if graph[vert + 1][hor] == 'X':  # if it's a wall
            down = None
        else:  # push down to queue
            queue.append([vert + 1, hor])
            graph[vert + 1][hor] += graph[vert][hor] + 1

    # update up
    if vert == 0:  # we're at top of graph. nothing to add to top
        up = None
    else:
        if graph[vert - 1][hor] == 'X':  # if it's a wall
            down = None
        else:  # push down to tovisit.
            queue.append([vert - 1, hor])
            graph[vert - 1][hor] += graph[vert][hor] + 1

    # update right
    if hor == rowlength:  # we're at right of graph. nothing to add to right
        right = None
    else:
        if graph[vert][hor + 1] == 'X':  # if it's a wall
            right = None
        else:  # push down to tovisit.
            queue.append([vert, hor + 1])
            graph[vert][hor + 1] += graph[vert][hor] + 1

    # update left
    if hor == 0:  # we're at left of graph. nothing to add to left
        left = None
    else:
        if graph[vert][hor - 1] == 'X':  # if it's a wall
            left = None
        else:  # push down to tovisit.
            queue.append([vert, hor - 1])
            graph[vert][hor - 1] += graph[vert][hor] + 1

    # then, until queue is empty, investigate each node in queue, then pop
    # if queue is empty, it means we've investigated each node that can be reached
    while len(queue) > 0:
        pos = queue.pop(0)
        vert = pos[0]
        hor = pos[1]

        # if destination is reached, search is over. call pathfinder
        if vert == destination[0] and hor == destination[1]:
            return findPath(graph, starting_vertex, destination)

        # update down
        if vert == columnheight:  # we're at bottom of graph. nothing to add to bottom
            down = None
        else:
            if graph[vert + 1][hor] == 'X' or graph[vert + 1][hor] != 0:  # if it's a wall or it's been visited
                down = None
            else:  # push down to queue
                queue.append([vert + 1, hor])
                graph[vert + 1][hor] += graph[vert][hor] + 1

        # update up
        if vert == 0:  # we're at top of graph. nothing to add to top
            up = None
        else:
            if graph[vert - 1][hor] == 'X' or graph[vert - 1][hor] != 0:  # if it's a wall or it's been visited
                down = None
            else:  # push down to queue
                queue.append([vert - 1, hor])
                graph[vert - 1][hor] += graph[vert][hor] + 1

        # update right
        if hor == rowlength:  # we're at right of graph. nothing to add to right
            right = None
        else:
            if graph[vert][hor + 1] == 'X' or graph[vert][hor + 1] != 0:  # if it's a wall or it's been visited
                right = None
            else:  # push down to tovisit.
                queue.append([vert, hor + 1])
                graph[vert][hor + 1] += graph[vert][hor] + 1

        # update left
        if hor == 0:  # we're at left of graph. nothing to add to left
            left = None
        else:
            if graph[vert][hor - 1] == 'X' or graph[vert][hor - 1] != 0:  # if it's a wall
                left = None
            else:  # push down to queue
                queue.append([vert, hor - 1])
                graph[vert][hor - 1] += graph[vert][hor] + 1

        if len(queue) > 0:
            if queue[-1] == [starting_vertex[0], starting_vertex[1]]:
                queue.pop(-1)
        graph[starting_vertex[0]][starting_vertex[1]] = 0  # just do this manually
    return None  # queue was emptied and destination was not reached


# helper that backtracks from destination to end and returns vertices visited
def findPath(graph, start, end):
    """
    Once all the steps have been mapped and the destination has been arrived at, this function backtracks
    and finds the optimal route that the previous function has found.
    """
    # to go right/left, graph[c][+/-1]
    # to go down/up, graph[+/-1][c]
    pos = [end[0], end[1]]
    route = []

    while pos[0] != start[0] or pos[1] != start[1]:  # while we are not back at the beginning
        route.append((pos[0], pos[1]))

        right = None
        left = None
        up = None
        down = None

        # update down
        if pos[0] + 1 > len(graph) - 1:
            down is None
        else:
            down = graph[pos[0] + 1][pos[1]]
        # update up
        if pos[0] - 1 < 0:
            up is None
        else:
            up = graph[pos[0] - 1][pos[1]]

        # update left
        if pos[1] - 1 < 0:
            left is None
        else:
            left = graph[pos[0]][pos[1] - 1]

        # # update right
        if pos[1] + 1 > len(graph[0]) - 1:
            right is None
        else:
            right = graph[pos[0]][pos[1] + 1]

        if left is not None and left == graph[pos[0]][pos[1]] - 1:
            pos = [pos[0], pos[1] - 1]
        elif right is not None and right == graph[pos[0]][pos[1]] - 1:
            pos = [pos[0], pos[1] + 1]
        elif up is not None and up == graph[pos[0]][pos[1]] - 1:
            pos = [pos[0] - 1, pos[1]]
        elif down is not None and down == graph[pos[0]][pos[1]] - 1:
            pos = [pos[0] + 1, pos[1]]

    route.append((start[0], start[1]))
    route.reverse()

    # prints directions followed as a string
    directions = []
    j = 1
    while j < len(route):
        if route[j-1][0] == route[j][0] + 1:
            directions.append('U')
        elif route[j-1][0] == route[j][0] - 1:
            directions.append('D')
        elif route[j-1][1] == route[j][1] + 1:
            directions.append('L')
        elif route[j-1][1] == route[j][1] - 1:
            directions.append('R')
        j += 1
    joined = "".join(directions)
    ecroute = (route, joined)
    return ecroute
