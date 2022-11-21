directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
ISLAND = "1"

class Solution:      

    def is_in_bounds(self, grid, row, col):

        num_rows = len(grid)
        num_cols = len(grid[0])

        row_in_bounds = row >=0 and row < num_rows
        col_in_bounds = col >=0 and col < num_cols

        return row_in_bounds and col_in_bounds

    def get_neighbors(self, grid, row, col):

        neighbors = []

        for row_offset, col_offset in directions:

            new_row = row + row_offset
            new_col = col + col_offset

            if not self.is_in_bounds(grid, new_row, new_col):
                continue            

            if grid[new_row][new_col] != ISLAND:
                continue
            
            new_neighbor = (new_row, new_col)
            neighbors.append(new_neighbor)        
        
        return neighbors 


    def mark_number_of_islands(self, grid, visited, row, col):
        
        position = (row, col)

        if position in visited:
            return
        
        visited.add(position)            

        neighbors = self.get_neighbors(grid, row, col)        
        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            if neighbor not in visited:
                self.mark_number_of_islands(grid, visited, neighbor_row, neighbor_col)

    def numIslands(self, grid: List[List[str]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        num_islands = 0

        visited = set()

        for row in range(num_rows):
            for col in range(num_cols):                
                if (row, col) not in visited and grid[row][col] == ISLAND:                    
                    num_islands += 1
                    self.mark_number_of_islands(grid, visited, row, col)
        
        return num_islands 