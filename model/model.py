import networkx as nx
from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def _buildGraph(self, year):
        self._graph = nx.Graph()
        self._graph.add_edges_from(DAO._getStatiVicinanze(year))
        return self._graph.number_of_nodes(), self._graph.number_of_edges(), nx.number_connected_components(self._graph)

    def _getGraphInfos(self):
        result = []
        for node in self._graph:
            result.append((node, self._graph.degree(node)))
        result.sort()
        return result

    def _getConnectedComponentNode(self, node):
        cc = list(nx.node_connected_component(self._graph, node))
        cc.remove(node)
        cc.sort()
        return cc