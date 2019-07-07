import os
import csv

class Node:
    def __init__(self, node, parent, depth):
        self.node = node
        self.parent = parent
        self.depth = depth

    def __str__(self):
        return "{0}\t{1}\t{2}".format(self.node, self.parent, self.depth)


def get_file():
    menu_select = int(input("Select graph file:\n(1) File from graph folder\n(2) Enter file path\n"))

    while 2 <= menu_select <=1:
        menu_select = int(input("Invalid selection, please try again:"))

    if menu_select == 1:
        print("Please select from the following files:")
        file_list = os.listdir("graphs")

        i = 1
        for file in file_list:
            print("\t" + str(i) + ")" + file)
            i+=1
        menu_select = int(input()) -1

        while not 0<= menu_select <= len(file_list):
            menu_select = int(input("Invalid selection, please try again:")) - 1

        file_path = "graphs/" + file_list[menu_select]

    else:
        file_path = input("Enter the location of the graph files")

        #Check that the file exists
        while not os.path.isfile(file_path):
            print("This is not a valid file, please try again")
            file_path = input("Enter the location of the graph files")

    return file_path


def find_node(node, graph):
    children = []
    for edge in graph:
        for i in range(0, 2):
            if edge[i] == node:
                children.append(edge[abs(i-1)])
    children.sort()
    return children


def find_unvisited(node, graph, visited):
    children = []
    for edge in graph:
        for i in range(0, 2):
            if edge[i] == node and edge[abs(i-1)] not in visited:
                children.append(edge[abs(i-1)])
    children.sort()
    return children


def find_node_obj(node, graph, depth, visited):
    children = []

    for edge in graph:
        for i in range(0, 2):
            if edge[i] == node and edge[abs(i-1)] not in visited:
                children.append(Node(edge[abs(i-1)], node, depth))
    children.sort(key=lambda x: x.node)
    return children


def find_unvisited_parent(node, graph, visited):
    children = []
    for edge in graph:
        for i in range(0, 2):
            if edge[i] == node and edge[abs(i-1)] not in visited:
                children.append((node , edge[abs(i-1)]))
    children.sort()
    return children


def print_list(list):
    for line in list:
        print(line)

'''
# depth first search-no recursive
def dfs(graph, start_node, end_node):
    visited = []
    children = find_node(start_node, graph)
    next_node = start_node
    visited.append(start_node)

    while next_node != end_node and children:
        next_node = children[0]
        visited.append(next_node)
        children = find_unvisited(next_node, graph, visited)

    if next_node == end_node:
        print("Goal node found")

    return visited
'''

# depth first search recursive
def dfs(graph, start_node, end_node):
    visited = []
    path = []
    children = find_node(start_node, graph)
    next_node = start_node
    path.append(start_node)
    visited.append(start_node)

    while next_node != end_node and children:
        next_node = children[0]
        path.append(next_node)
        visited.append(next_node)
        children = find_unvisited(next_node, graph, visited)
        if not children and path[-1] != start_node and next_node != end_node:
            path.pop()
            children = find_unvisited(path[-1], graph, visited)

    if next_node == end_node:
        print("Goal path found")
    else:
        print("Goal path not found")

    return visited


def bfs(graph, start_node, end_node):
    goal_found = False
    next_node = start_node
    visited = [start_node]
    to_search = [start_node]
    temp = []
    children = []
    next_depth = []

    while not goal_found and to_search:
        print("gets here")
        for node in to_search:
            temp = find_unvisited(node, graph, visited)
            children.extend(temp)
            visited.extend(temp)
            next_depth.extend(temp)
        to_search = next_depth.copy()
        print(to_search)
        next_depth.clear()
        print(to_search)
        if end_node in visited:
            goal_found = True
            print("Goal found")
    print(visited)


# Iterative deepening search
def ids(graph, start_node, end_node):
    visited = [start_node]
    path = [Node(start_node, None, 0)]

    path.extend(find_node_obj(start_node, graph, 1, visited))

    for vis_node in path:
        print(vis_node)


file_path = get_file()

graph_file = open(file_path, "r")
print("File readable: " + str(graph_file.readable()))

graph = list(csv.reader(graph_file, delimiter=' '))

print_list(graph)

start_node = graph[0][0]
end_node = graph[0][1]
print("Start node: " + start_node + "\nEnd node: " + end_node)
graph.pop(0)

'''
print("Depth first search:")
print(dfs(graph, start_node, end_node))
'''
'''
print("Breadth first search")
bfs(graph, start_node, end_node)
'''

print("Iterative deepening search:")
ids(graph, start_node, end_node)

graph_file.close()