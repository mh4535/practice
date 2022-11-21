from collections import defaultdict

UNVISITED = 0
PREVIOUSLY_VISITED = 1
CURRENTLY_VISITING = -1
CAN_FINISH = True

class Solution:  

    def build_graph(self, prerequisites):

        graph = defaultdict(list)

        for course, prereq in prerequisites:

            graph[prereq].append(course)

        return graph   

    def is_sequence_from_this_node_valid(self, graph, visited, course):

        #Base case
        if visited[course] == CURRENTLY_VISITING:
            return False

        #Process node
        visited[course] = CURRENTLY_VISITING

        #Recurse on neighbors
        neighbors = graph[course]
        for neighbor in neighbors:

            if visited[neighbor] == PREVIOUSLY_VISITED:
                continue

            is_path_valid = self.is_sequence_from_this_node_valid(graph, visited, neighbor)
            
            if not is_path_valid:
                return False 

        visited[course] = PREVIOUSLY_VISITED

        return CAN_FINISH



    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:

        graph = self.build_graph(prerequisites)

        visited = [UNVISITED for i in range(num_courses)]

        for course in range(num_courses):

            if visited[course] == PREVIOUSLY_VISITED:
                continue
            
            is_sequence_from_this_node_valid = self.is_sequence_from_this_node_valid(graph, visited, course)

            if not is_sequence_from_this_node_valid:
                return False

        return CAN_FINISH