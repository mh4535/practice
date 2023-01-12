from collections import deque

directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2)]

class Solution:
    
    def get_neighbors(self, row, col):
        
        neighbors = []       
        
        for row_offset, col_offset in directions:
            new_row = row_offset + row
            new_col = col_offset + col
            
            new_neighbor = (new_row, new_col)
            neighbors.append(new_neighbor) 
        
        return neighbors
    
    def minKnightMoves(self, target_row: int, target_col: int) -> int:
        
        queue = deque()
        
        start_position = (0, 0)
        distance_from_start = 0
        start_tuple = (start_position, distance_from_start)
        queue.append(start_tuple)
        
        visited = set()
        visited.add(start_position)
        
        while queue:
            
            position, distance = queue.popleft()
            row, col = position
            
            if row == target_row and col == target_col:
                return distance            
            
            neighbors = self.get_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)    
                
                new_neighbor = (neighbor, distance + 1)
                queue.append(new_neighbor)