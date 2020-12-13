#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import networkx as nx
import math

Directory = "Desktop/Input_Conversion/Edgelist_New/"
file ="usca150"
ext ="_conv.txt"
filename = Directory+file+ext
G = nx.read_edgelist(filename, nodetype=int, data=(("weight", float),), create_using=nx.DiGraph)
#print(G.edges(data=True))
source = int(input())
destination = int(input())

def select_random_path(G, source, destination):
    neighbors_init = [i for i in range(0,nx.number_of_nodes(G))]
    neighbors_init.remove(source)
#     print(neighbors_init)
#     print(random.choice(neighbors_init))
    path = [source]
    neighbor = -1
    path_lens = []
    source_now = source

    while neighbor!=destination:
        neighbor = random.choice(neighbors_init)
        if G.has_edge(source_now, neighbor):
            path_lens.append(G.get_edge_data(source_now,neighbor).get('weight'))
#         elif G.has_edge(neighbor, source_now):
#             path_lens.append(G.get_edge_data(neighbor,source_now).get('weight'))
        else:
            path_lens.append(-999)
        source_now=neighbor
        neighbors_init.remove(source_now)
#         print(neighbors_init)
        path.append(neighbor)

    #print(path)
#     print(path_lens)
    #print(sum(path_lens))
    return path, sum(path_lens)
    
temp_init = 1150
temp_final = 800
itermax = 25

def Anneal(G, source, destination, temp_init, temp_final, itermax):
    #print("initial state:")
    P, length_p = select_random_path(G, source, destination)
    #print("Path:", P)
    #print("Length:", length_p)
    temp = temp_init
    best_path_lens = []
    best_path = P
    best_len = length_p
    while temp >= temp_final:
        iteration = 0
        while iteration  < itermax:
            S, length_s = select_random_path(G, source, destination)
            if length_s > best_len:
                best_path = S
                best_len = length_s
            
            delta = length_s - length_p
            if delta > 0:
                P = S
                length_p = length_s
            else:
                x = random.random()
                prob = math.exp(delta / temp)
                #print(x)
                #print(prob)
                if x < prob:
                    P = S
                    length_p = length_s
            
            #print("Temp:", temp, "iteration:", iteration)
            #print("Path:", S, "Length:", length_s)
            
            #print()
            iteration = iteration + 1
        
        best_path_lens.append(length_p)
        temp = temp-1
        #print()
        #print()
        #print()
    
    print(file)
    #print(best_path_lens)
    #print("Length: ", max(best_path_lens))
    print("Length: ", best_len)
    #print(min([i for i in best_path_lens if i > 0]))
    print("Path: ", best_path)
    
Anneal(G, source, destination, temp_init, temp_final, itermax)


# In[ ]:




