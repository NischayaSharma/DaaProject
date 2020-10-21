import networkx as nx
import matplotlib.pyplot as plt


class GraphUtils:

    def createGraph(self, graph):
        G = nx.Graph()
        G.add_nodes_from(graph.keys())
        for k, v in graph.items():
            for vv in v:
                G.add_edge(k, vv[0], weight=vv[1])
        pos = nx.random_layout(G)
        eLabels = nx.get_edge_attributes(G, 'weight')
        return [G, pos, eLabels]
    
    def displayGraph(self, G, pos, labels, eLabels, name):
        nx.draw(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=eLabels)
        nx.draw_networkx_labels(G, pos, labels, font_size=10)
        plt.savefig("./media/"+name)
        plt.show()

    def createGraphFromPath(self, G, path, labels):
        graph = nx.Graph()
        weights = nx.get_edge_attributes(G, 'weight')
        for key, value in path.items():
            if len(value) >= 1:
                for i in range(len(value)-1):

                    if value[i] not in list(graph.nodes):
                        graph.add_node(value[i])
                    if value[i] not in list(graph.nodes):
                        graph.add_node(value[i+1])
                    try:
                        graph.add_edge(value[i], value[i+1],
                                       weight=weights[(value[i], value[i+1])])
                    except KeyError:
                        graph.add_edge(value[i], value[i+1],
                                       weight=weights[(value[i+1], value[i])])
        eLabels = nx.get_edge_attributes(graph, 'weight')
        return graph, labels, eLabels
