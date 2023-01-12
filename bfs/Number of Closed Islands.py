from collections import deque

LAND = 0

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:

    def is_on_edge(self, grid, row, col):

        num_rows = len(grid)
        num_cols = len(grid[0])

        for row_offset, col_offset in directions:
            new_row = row_offset + row
            new_col = col_offset + col

            if not self.is_in_bounds(grid, new_row, new_col):
                print(row, col)
                return True

        return False


    def is_in_bounds(self, grid, row, col):

        num_rows = len(grid)
        num_cols = len(grid[0])

        row_in_bounds = row >= 0 and row < num_rows
        col_in_bounds = col >= 0 and col < num_cols

        return row_in_bounds and col_in_bounds
        

    def get_neighbors(self, grid, row, col):

        neighbors = []

        for row_offset, col_offset in directions:
            new_row = row_offset + row
            new_col = col_offset + col

            if not self.is_in_bounds(grid, new_row, new_col):
                continue

            if grid[new_row][new_col] != LAND:
                continue
            
            new_neighbor = (new_row, new_col)
            neighbors.append(new_neighbor)
    
        return neighbors

    def mark_component_and_identify_if_closed(self, grid, row, col, visited):

        queue = deque()

        initial_position = (row, col)
        queue.append(initial_position)

        visited.add(initial_position)

        is_island_closed = True

        while queue:

            #Pop node
            position = queue.popleft()
            current_row, current_col = position

            #Process node
            if self.is_on_edge(grid, current_row, current_col):
                print("not closed")
                print(current_row, current_col)
                is_island_closed = False


            #Get node neighbors
            neighbors = self.get_neighbors(grid, current_row, current_col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)

                queue.append(neighbor)

        return is_island_closed


    def closedIsland(self, grid: List[List[int]]) -> int:

        num_closed_islands = 0
    
        visited = set()

        num_rows = len(grid)
        num_cols = len(grid[0])

        for row in range(num_rows):
            for col in range(num_cols):
                position = (row, col)
                if grid[row][col] == LAND and position not in visited:
                    is_connected_component_closed = self.mark_component_and_identify_if_closed(grid, row, col, visited)
                    if is_connected_component_closed:
                        num_closed_islands += 1

        return num_closed_islands