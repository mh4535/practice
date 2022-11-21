#This solution times out on some tests.


from collections import defaultdict 
NOT_ALL_NODES_ARE_REACHABLE = -1

class Solution:

    def build_graph(self, times):

        graph = defaultdict(dict)

        for source, dest, time in times:
            graph[source][dest] = time
        
        return graph 

    def get_minimum_time_for_signal(self, graph, minimum_time_to_be_reached, node, time_so_far):

        if time_so_far >= minimum_time_to_be_reached[node]:
            return 
        
        minimum_time_to_be_reached[node] = time_so_far

        neighbors = graph[node]
        for neighbor in neighbors:

            time_to_reach_this_neighbor = graph[node][neighbor]

            self.get_minimum_time_for_signal(graph, minimum_time_to_be_reached, neighbor, time_to_reach_this_neighbor + time_so_far)

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        graph = self.build_graph(times)

        minimum_time_to_be_reached = [float('inf') for node in range(n + 1)]
        minimum_time_to_be_reached[0] = -float('inf')

        initial_time = 0

        self.get_minimum_time_for_signal(graph, minimum_time_to_be_reached, k, initial_time)

        total_time = max(minimum_time_to_be_reached)

        if total_time == float('inf'):
            return NOT_ALL_NODES_ARE_REACHABLE


        return int(total_time)