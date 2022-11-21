START_NODE = 0
class Solution:
    
    def get_paths_from_source_to_dest(self, graph, all_paths_to_target, path_from_curr_node, curr_node, target):
        
        path_copy = path_from_curr_node.copy()
        path_copy.append(curr_node)

        if curr_node == target:
            all_paths_to_target.append(path_copy)        

        neighbors = graph[curr_node]
        for neighbor in neighbors:          

            self.get_paths_from_source_to_dest(graph, all_paths_to_target, path_copy, neighbor, target)



    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

       all_paths_to_target = []

       path_from_curr_node = []

       target = len(graph) - 1

       self.get_paths_from_source_to_dest(graph, all_paths_to_target, path_from_curr_node, START_NODE, target)

       return all_paths_to_target