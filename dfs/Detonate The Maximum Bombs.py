from collections import defaultdict  
import math 

class Solution:

    def bomb_radii_overlap(self, first_x, first_y, first_radius, second_x, second_y, second_radius):        

        x_diff = first_x - second_x
        y_diff = first_y - second_y

        distance_btwn_centers = math.sqrt(x_diff**2 + y_diff**2)

        if distance_btwn_centers <= first_radius:
            return True
        
        return False  


    def build_graph(self, bombs):

        graph = defaultdict(list)

        for i in range(len(bombs) - 1):
            first_x, first_y, first_z = bombs[i]
            for j in range(i + 1, len(bombs)):
                second_x, second_y, second_z = bombs[j]
                if self.bomb_radii_overlap(first_x, first_y, first_z, second_x, second_y, second_z):
                    graph[i].append(j)
                if self.bomb_radii_overlap(second_x, second_y, second_z, first_x, first_y, first_z):
                    graph[j].append(i)
        
        return graph 

    def get_num_bombs_detonated_from_curr_bomb(self, graph, visited, bomb):

        if bomb in visited:
            return 0  
        
        visited.add(bomb)

        num_bombs_detonated_from_curr_bomb = 1               

        neighbors = graph[bomb]
        for neighbor in neighbors:
            if neighbor not in visited:
                num_bombs_detonated_from_curr_bomb += self.get_num_bombs_detonated_from_curr_bomb(graph, visited, neighbor)        
        
        return num_bombs_detonated_from_curr_bomb

    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = self.build_graph(bombs)            

        max_num_bombs_detonated = 0
        
        for bomb in range(len(bombs)):            
            visited = set()
            num_bombs_detonated_from_curr_bomb = self.get_num_bombs_detonated_from_curr_bomb(graph, visited, bomb)
            max_num_bombs_detonated = max(max_num_bombs_detonated, num_bombs_detonated_from_curr_bomb)
        
        return max_num_bombs_detonated