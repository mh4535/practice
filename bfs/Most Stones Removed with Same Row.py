from collections import deque
from collections import defaultdict

STONE = 1

class Solution:

    def build_graph(self, stones):

        stone_set = set()
        for stone_position in stones:
            stone_row = stone_position[0]
            stone_col = stone_position[1]
            stone_tuple = (stone_row, stone_col)
            stone_set.add(stone_tuple)
        
        graph = defaultdict(list)

        for stone_position in stone_set:
            for possible_neighbor in stones:
                if stone_position == possible_neighbor:
                    continue
                stone_row, stone_col = stone_position
                possible_neighbor_row, possible_neighbor_col = possible_neighbor
                if stone_row == possible_neighbor_row or stone_col == possible_neighbor_col:
                    possible_neighbor_tuple = (possible_neighbor_row, possible_neighbor_col)
                    graph[stone_position].append(possible_neighbor_tuple)
        
        return graph
    
    

        '''
        1 0 1
        0 1 0
        1 0 1        
        '''

    def get_max_num_of_removable_stones_for_component(self, stones, graph, visited, initial_stone_position):
        
        max_num_stones = 0
        
        visited.add(initial_stone_position)

        queue = deque()
        queue.append(initial_stone_position)

        while queue:
           
            position = queue.popleft()
                        
            max_num_stones += 1
            
            neighbors = graph[position]
            print(neighbors)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)

                queue.append(neighbor)

        #Will have one stone left over in every conn. component, so subtract 1        
        return max_num_stones - 1


    def removeStones(self, stones: List[List[int]]) -> int:

        graph = self.build_graph(stones)
        
        num_graph_rows = len(graph)
        num_graph_cols = len(graph[0])

        stones_removed = 0

        visited = set()       

        for stone_position in stones:
            stone_row = stone_position[0]
            stone_col = stone_position[1]
            stone_tuple = (stone_row, stone_col)
            if stone_tuple not in visited:                
                stones_removed += self.get_max_num_of_removable_stones_for_component(stones, graph, visited, stone_tuple)

        return stones_removed