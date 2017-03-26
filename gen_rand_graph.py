# generates random graph for hw Checking

import random
import copy

def gen_single_graph(graph_size, s):
    a = random.Random()
    a.seed(s)
    a1 = [a.randint(0,1) for k in range(graph_size*graph_size/2)]
    graph = gen_blank_graph(graph_size)
    for i in range (graph_size):
        for j in range(i+1, graph_size):
            graph[i][j] = a1.pop()
            graph[j][i] = graph[i][j]
    print graph
    return graph

def gen_blank_graph(graph_size):
    g = []
    blank_l = []
    for i in range(graph_size):
        blank_l.append(0)
    for j in range(graph_size):
        g.append(copy.deepcopy(blank_l))
    return g        

def write_to_input(graph_size,f,graph):
    f.write(str(graph_size))
    f.write("\n")
    for i in range(graph_size):
        for j in range(graph_size):
            f.write(str(graph[i][j]))
            if j != graph_size-1:
                f.write(" ")
        f.write("\n")
    return

if __name__ == "__main__":
    lower_bound = 1
    upper_bound = 100
    graph_size = 12
    f = open("input.txt",'w')
    graph = gen_single_graph(graph_size,1)
    write_to_input(graph_size, f, graph)
    f.close()
