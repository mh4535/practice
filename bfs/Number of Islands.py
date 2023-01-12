from collections import deque

ISLAND = "1"
WATER = "0"

def is_in_bounds(grid, row, col):
        
        num_rows = len(grid)
        num_cols = len(grid[0]) 
        
        row_in_bounds = row >= 0 and row < num_rows
        col_in_bounds = col >= 0 and col < num_cols
        
        return row_in_bounds and col_in_bounds
    

class Solution:     
    
    def get_neighbors(self, grid, row, col):   
          
        neighbors = [] 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  

        
        for row_offset, col_offset in directions:            
            new_row = row + row_offset
            new_col = col + col_offset
            
            if not is_in_bounds(grid, new_row, new_col):
                continue
            
            if grid[new_row][new_col] == WATER:
                continue
            
            new_neighbor = (new_row, new_col)
            neighbors.append(new_neighbor)
        
        return neighbors
    
    def mark_islands_as_visited(self, grid, row, col, visited):
        
        initial_position = (row, col)
        
        queue = deque()
        queue.append(initial_position)
        
        visited.add(initial_position)
        
        while queue:
            
            position = queue.popleft()
            row, col = position
            
            neighbors = self.get_neighbors(grid, row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                                
                queue.append(neighbor)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:        
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        visited = set()
        
        for row in range(num_rows):
            for col in range(num_cols):
                position = (row, col)
                if grid[row][col] == ISLAND and position not in visited:
                    num_islands += 1                   
                    self.mark_islands_as_visited(grid, row, col, visited)
                    
        return num_islands