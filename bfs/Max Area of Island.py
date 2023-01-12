from collections import deque

ISLAND = 1
WATER = 0

class Solution:
    
    def is_in_bounds(self, grid, row, col):
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        row_in_bounds = row >= 0 and row < num_rows
        col_in_bounds = col >= 0 and col < num_cols
        
        return row_in_bounds and col_in_bounds
    
    def get_neighbors(self, grid, row, col):
        
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for row_offset, col_offset in directions:
            new_row = row + row_offset 
            new_col = col + col_offset
            
            if not self.is_in_bounds(grid, new_row, new_col):
                continue
            
            if grid[new_row][new_col] == WATER:
                continue
            
            new_neighbor = (new_row, new_col)
            neighbors.append(new_neighbor)
      
        return neighbors
        
    
    def get_island_area(self, grid, row, col, visited):
        
        queue = deque()
        
        initial_position = (row, col) 
        queue.append(initial_position)
        
        visited.add(initial_position)
        
        island_area = 0        
               
        while queue:
            
            position = queue.popleft()
            row, col = position           
            
            island_area += 1            
            
            neighbors = self.get_neighbors(grid, row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                
                queue.append(neighbor)
        
        return island_area
    
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        visited = set()
        max_area = 0
        
        for row in range(num_rows):
            for col in range(num_cols):
                position = (row, col)
                if grid[row][col] == ISLAND and position not in visited:
                    current_island_area = self.get_island_area(grid, row, col, visited)
                    max_area = max(max_area, current_island_area)
        
        return max_area
                    