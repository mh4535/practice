from collections import defaultdict

class Solution:

    def build_graph(self, edges):

        graph = defaultdict(list)

        for source, dest in edges:

            graph[source].append(dest)
            graph[dest].append(source)

        return graph 

    def mark_all_nodes_reachable_by_original_source(self, graph, visited, source):

        if source in visited:
            return

        visited.add(source)

        neighbors = graph[source]
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            self.mark_all_nodes_reachable_by_original_source(graph, visited, neighbor)
        


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = self.build_graph(edges)

        visited = set()

        self.mark_all_nodes_reachable_by_original_source(graph, visited, source)

        valid_path_exists = destination in visited

        return valid_path_exists 