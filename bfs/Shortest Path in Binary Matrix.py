from collections import deque

CLEAR = 0
NO_CLEAR_PATH = -1


class Solution:
    
    def in_bounds(self, row, col, grid):
        
        length = len(grid)
        
        row_in_bounds = row >= 0 and row < length
        col_in_bounds = col >= 0 and col < length
        
        return row_in_bounds and col_in_bounds      
    
    def get_neighbors(self, grid, curr_row, curr_col):
        
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        neighbors = []
        
        for row_offset, col_offset in directions:           
            new_row = curr_row + row_offset
            new_col = curr_col + col_offset
            
            if not self.in_bounds(new_row, new_col, grid):
                continue
            
            if grid[new_row][new_col] != CLEAR:
                continue
            
            new_position = (new_row, new_col)            
            neighbors.append(new_position)
        
        print(neighbors)
        return neighbors
            
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        initial_position = (0, 0)
        row, col = initial_position
        
        if grid[row][col] != CLEAR:
            return NO_CLEAR_PATH        
        
        length = len(grid)
        
        queue = deque()        
        initial_distance = 1
        initial_tuple = (initial_position, initial_distance)
        queue.append(initial_tuple)
                       
        visited = set()
        visited.add(initial_position)
                
        while queue:
            
            position, distance = queue.popleft() 
            row, col = position            
            
            if row == length - 1 and col == length - 1:
                return distance
            
            neighbors = self.get_neighbors(grid, row, col)            
            for neighbor in neighbors:                
                if neighbor in visited:
                    continue               
                visited.add(neighbor)
                
                new_neighbor = (neighbor, distance + 1)
                queue.append(new_neighbor)
                
        return NO_CLEAR_PATH