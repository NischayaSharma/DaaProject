class bellMan:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    # def printArr(self, dist):
    #     print("Vertex Distance from Source")
    #     for i in range(self.V):
    #         print("{0}\t\t{1}".format(i, dist[i]))

    # Recursive function to Obtain the path of every node all the way 
    # back to the source node
    def path(self, node, prev):
        if (prev[node] == 'source'):
            return []
        return self.path(prev[node], prev) + [prev[node]]

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0
        pred = {src: "source"}

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    # Storing the Parent node of every node to construct path
                    pred[v] = u

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        # self.printArr(dist)
        # print(pred)
        # print("\n\n\n")

        # The Dictionary which will contain the path of every node from the source node
        pathDict = {}
        
        # Tracing the parent node of every node back to the source node
        for key in pred.keys():
            path = self.path(key, pred)
            pathDict[key]=path
        # Adding the Destination node to the path for making the format similar to 
        # networkx's path output
        for key, val in pathDict.items():
            pathDict[key] = pathDict[key] + [key]
        # print(pathDict)
        return pathDict


# Driver Class for the BellmanFord algorithm above
class BellmanFord:
    def main(self,graph, source):
        g = bellMan(len(graph))
        for key, val in graph.items():
            for node in val:
                g.addEdge(key, node[0], node[1])
        return g.BellmanFord(source)