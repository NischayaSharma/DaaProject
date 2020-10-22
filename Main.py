import networkx as nx
import GraphUtils
import bellMan, Djikstra

gConf = GraphUtils.GraphUtils()
# graphWhereDjikstraFails = {0: [(1, -1), (2, -2)], 1: [(2, 3), (3, 2), (4, 2)], 2: [], 3: [(2, -5), (1, 1)], 4: [(3, 3)]}
graph = {0: [(1, -1), (2, -2)], 1: [(2, 3), (3, 2), (4, 2)], 2: [], 3: [(2, 5), (1, 1)], 4: [(3, 3)]}
labels = {0: "Hospital", 1: "Work", 2: "Shop", 3: "Grocery Store", 4: "Home"}
source = 0

def djikstra(gConf, graph, G, labels, pos, source):
    try:
        # Calculating shortest distances and shortest path
        # from source node to every node
        path = Djikstra.driver(graph, source)
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


G, _, eLabels = gConf.createGraph(graph)
pos = {0: ([0.06860986, 0.27299064]), 1: ([0.4623169 , 0.41947186]), 2: ([0.8904452 , 0.34492362]), 3: ([0.63216573, 0.8758493 ]), 4: ([0.305631 , 0.506014])}
# print(pos)
gConf.displayGraph(G=G, pos=pos, labels=labels,
                   eLabels=eLabels, name="originalGraph.jpeg")
djikstra(gConf=gConf, graph=graph, G=G, labels=labels, pos=pos, source=source)
bellmanFord(gConf=gConf, graph=graph, G=G,
            labels=labels, pos=pos, source=source)
