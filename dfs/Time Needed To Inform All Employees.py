from collections import defaultdict 
OWN_BOSS = -1

class Solution:

    def build_graph(self, employee_hierarchy):

        graph = defaultdict(list)

        for employee_id in range(len(employee_hierarchy)):

            manager_of_curr_employee = employee_hierarchy[employee_id]

            if manager_of_curr_employee == OWN_BOSS:
                continue

            graph[manager_of_curr_employee].append(employee_id)
        
        return graph 
    

    def get_time_to_inform_everyone(self, graph, inform_time, employee_id, time_so_far):

        if employee_id not in graph:
            return time_so_far 

        max_time = time_so_far

        neighbors = graph[employee_id]
        for neighbor in neighbors:

            time_needed_to_inform_subordinates = self.get_time_to_inform_everyone(graph, inform_time, neighbor, time_so_far + inform_time[employee_id])

            max_time = max(max_time, time_needed_to_inform_subordinates)

        return max_time  


    def numOfMinutes(self, n: int, head_id: int, employee_hierarchy: List[int], inform_time: List[int]) -> int:

        graph = self.build_graph(employee_hierarchy)

        initial_time = 0

        return self.get_time_to_inform_everyone(graph, inform_time, head_id, initial_time)