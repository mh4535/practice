from collections import deque

NO_VALID_COURSE_SCHEDULE = []

class Solution:
    
    def build_graph_and_indegree_map(self, num_courses, prereqs):

        graph = defaultdict(list)

        indegree_map = {}
        for course in range(num_courses):
            indegree_map[course] = 0            

        for course, prereq in prereqs:
            graph[prereq].append(course)
            indegree_map[course] += 1
        
        return graph, indegree_map

    def get_queue_for_nodes_with_zero_indegree(self, indegree_map):

        queue_nodes_with_zero_indegree = deque()

        for course in indegree_map:
            if indegree_map[course] == 0:
                queue_nodes_with_zero_indegree.append(course)
        
        return queue_nodes_with_zero_indegree

    def get_valid_ordering(self, graph, indegree_map):

        valid_ordering = []

        queue_nodes_with_zero_indegree = self.get_queue_for_nodes_with_zero_indegree(indegree_map)

        while queue_nodes_with_zero_indegree:

            #pop
            course = queue_nodes_with_zero_indegree.popleft()

            #process
            valid_ordering.append(course)

            #add neighbors
            neighbors = graph[course]
            for neighbor in neighbors:
                indegree_map[neighbor] -= 1
                
                if indegree_map[neighbor] == 0:
                    queue_nodes_with_zero_indegree.append(neighbor)
        
        return valid_ordering

    def findOrder(self, num_courses: int, prereqs: List[List[int]]) -> List[int]:

        graph, indegree_map = self.build_graph_and_indegree_map(num_courses, prereqs) 

        valid_ordering = self.get_valid_ordering(graph, indegree_map)

        if len(valid_ordering) < num_courses:
            return NO_VALID_COURSE_SCHEDULE

        return valid_ordering