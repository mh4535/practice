from collections import defaultdict 
 
class Solution:

    def build_graph(self, pid, ppid):

        graph = defaultdict(list)

        num_processes = len(ppid)

        for i in range(num_processes):

            parent_process_id = ppid[i]
            child_process_id = pid[i]

            if parent_process_id == 0:
                continue 

            graph[parent_process_id].append(child_process_id)
        
        return graph 

    def mark_all_child_processes(self, graph, visited, process):

        if process in visited:
            return      
        
        visited.add(process)

        if process not in graph:
            return 

        neighbors = graph[process]
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            self.mark_all_child_processes(graph, visited, neighbor)

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        graph = self.build_graph(pid, ppid)

        visited = set()

        self.mark_all_child_processes(graph, visited, kill)

        killed_processes_list = []
        for process in visited:
            killed_processes_list.append(process)

        return killed_processes_list