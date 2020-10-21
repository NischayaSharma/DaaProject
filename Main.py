import networkx as nx
import GraphUtils
import bellMan

# Method to calculate the Single source dijkstra and Display it
# It prints if the graph contains negative weights


def djikstra(gConf, G, labels, pos, source):
    try:
        # Calculating shortest distances and shortest path
        # from source node to every node
        length, path = nx.single_source_dijkstra(G, source)
        # Creating graph from the above obtained path
        djiGraph, labels, eLabels = gConf.createGraphFromPath(G, path, labels)
        # Displaying the above created graph
        gConf.displayGraph(G=djiGraph, name="djikstraPath.jpeg",
                           labels=labels, eLabels=eLabels, pos=pos)
    except ValueError:
        print("Negative Weights not allowed in Djikstra")


def bellmanFord(gConf, graph, G, labels, pos, source):
    
    bell = bellMan.BellmanFord()
    path = bell.main(graph, source)
    graph, labels, eLabels = gConf.createGraphFromPath(G, path, labels)
    gConf.displayGraph(G=graph, name="bellManPath.jpeg",
                       labels=labels, eLabels=eLabels, pos=pos)


gConf = GraphUtils.GraphUtils()
graph = {0: [(1, -1), (2, -2)], 1: [(2, 3), (3, 2), (4, 2)],
         2: [], 3: [(2, 5), (1, 1)], 4: [(3, 3)]}
labels = {0: "Home", 1: "Work", 2: "Shop",
          3: "Grocery Store", 4: "Hello World"}
source = 0
G, pos, eLabels = gConf.createGraph(graph)
gConf.displayGraph(G=G, pos=pos, labels=labels,
                   eLabels=eLabels, name="originalGraph.jpeg")
djikstra(gConf=gConf, G=G, labels=labels, pos=pos, source=source)
bellmanFord(gconf=gConf, graph=graph, G=G,
            labels=labels, pos=pos, source=source)
