from collections import deque
import sys

LAND = 1
MAX_VALUE = sys.maxsize

directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

class Solution:

    def is_in_bounds(self, grid, row, col):

        num_rows = len(grid)
        num_cols = len(grid[0])

        is_row_in_bounds = row >= 0 and row < num_rows
        is_col_in_bounds = col >= 0 and col < num_cols

        return is_row_in_bounds and is_col_in_bounds
        

    def get_first_island_neighbors(self, grid, row, col):

        neighbors = []

        for row_offset, col_offset in directions:

            new_row = row + row_offset
            new_col = col + col_offset

            if not self.is_in_bounds(grid, new_row, new_col):
                continue
            
            if grid[new_row][new_col] != LAND:
                continue
            
            new_neighbor = (new_row, new_col)
            neighbors.append(new_neighbor)
        
        return neighbors
        
    def get_second_neighbors(self, grid, row, col, first_visited_set):

        neighbors = []

        for row_offset, col_offset in directions:

            new_row = row + row_offset
            new_col = col + col_offset

            new_position = (new_row, new_col)

            if not self.is_in_bounds(grid, new_row, new_col):
                continue
            
            if new_position in first_visited_set:
                continue
            
            neighbors.append(new_position)

        return neighbors

    def get_distance_between_islands(self, grid, first_visited_set):

        distance_set = set()        

        for position in first_visited_set:
            row, col = position

            queue = deque()

            initial_distance = 0

            initial_tuple = (position, initial_distance)
            queue.append(initial_tuple) 

            second_visited_set = set()                             

            while queue:

                #pop
                position, distance = queue.popleft()
                row, col = position                   
                is_from_first_island = distance == 0                          

                #process
                already_have_distances = len(distance_set) > 0
                if already_have_distances:
                    if distance > min(distance_set):
                        break

                if grid[row][col] == LAND and not is_from_first_island:
                    distance_set.add(distance)                        
                    break               

                #get neighbors
                neighbors = self.get_second_neighbors(grid, row, col, first_visited_set)
                for neighbor in neighbors:
                    if neighbor in first_visited_set or neighbor in second_visited_set:
                        continue
                    second_visited_set.add(neighbor)

                    new_neighbor = (neighbor, distance + 1)
                    queue.append(new_neighbor)
            
        return min(distance_set) - 1

    def populate_first_visited_set(self, grid, first_visited_set, first_row, first_col):

        queue = deque()

        initial_position = (first_row, first_col)

        queue.append(initial_position)

        first_visited_set.add(initial_position)

        while queue:

            #Pop node
            position = queue.popleft()
            row, col = position
            
            # get neighbors
            neighbors = self.get_first_island_neighbors(grid, row, col)
            for neighbor in neighbors:
                if neighbor in first_visited_set:
                    continue
                first_visited_set.add(neighbor)
            
                queue.append(neighbor)      


    def shortestBridge(self, grid: List[List[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        first_land_position = (0, 0)

        #Get first land position
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == LAND:
                    first_land_position = (row, col)
        

        first_row, first_col = first_land_position

        first_visited_set = set()   

        distance_between_islands = 0

        self.populate_first_visited_set(grid, first_visited_set, first_row, first_col)  
            
        
        distance_between_islands = self.get_distance_between_islands(grid, first_visited_set)

        return distance_between_islands


        