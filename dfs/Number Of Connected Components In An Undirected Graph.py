from collections import defaultdict

class Solution:

    def build_graph(self, edges):

        graph = defaultdict(list)

        for point_one, point_two in edges:

            graph[point_one].append(point_two)
            graph[point_two].append(point_one)
        
        return graph 

    def find_points_in_current_component(self, graph, visited, curr_node):
        
        visited.add(curr_node)       

        neighbors = graph[curr_node]
        for neighbor in neighbors:
            if neighbor not in visited:   
                visited.add(neighbor)    
                         
                self.find_points_in_current_component(graph, visited, neighbor)


    def countComponents(self, num_nodes: int, edges: List[List[int]]) -> int:

        graph = self.build_graph(edges)

        num_components = 0

        visited = set()

        for node in range(num_nodes):
            if node not in visited:
                num_components += 1
                self.find_points_in_current_component(graph, visited, node)

        return num_components 