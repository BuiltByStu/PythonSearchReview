import os
import csv


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
    return children


def find_unvisited(node, graph, visited):
    children = []
    for edge in graph:
        for i in range(0, 2):
            if edge[i] == node and edge[abs(i-1)] not in visited:
                children.append(edge[abs(i-1)])
    return children


def print_list(list):
    for line in list:
        print(line)


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


file_path = get_file()

graph_file = open(file_path, "r")
print("File readable: " + str(graph_file.readable()))

graph = list(csv.reader(graph_file, delimiter=' '))

print_list(graph)

start_node = graph[0][0]
end_node = graph[0][1]
print("Start node: " + start_node + "\nEnd node: " + end_node)
graph.pop(0)


print("Depth first search:")
print(dfs(graph, start_node, end_node))

graph_file.close()