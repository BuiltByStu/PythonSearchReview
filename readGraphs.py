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
    for edge in graph:
        for i in range(0, 2):
            if edge[i] == node:
                print(edge[abs(i-1)]) #This node is connected to the node being searched for


def print_list(list):
    for line in list:
        print(line)


start_node = []
end_node = []

file_path = get_file()


graph_file = open(file_path, "r")
print("File readable: " + str(graph_file.readable()))

graph = list(csv.reader(graph_file, delimiter=' '))

print_list(graph)

start_node = graph[0][0]
end_node = graph[0][1]
print("Start node: " + start_node + "\nEnd node: " + end_node)
graph.pop(0)

find_node(start_node, graph)

graph_file.close()