from collections import deque

ROTTEN = 2
FRESH = 1
EMPTY = 0
NOT_POSSIBLE = -1

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:

    def is_in_bounds(self, grid, row, col):

      num_rows = len(grid)
      num_cols = len(grid[0])

      is_row_in_bounds = row >= 0 and row < num_rows
      is_col_in_bounds = col >= 0 and col < num_cols

      return is_row_in_bounds and is_col_in_bounds

    def get_neighbors(self, grid, row, col):    

      neighbors = []

      for row_offset, col_offset in directions:
        
        new_row = row + row_offset
        new_col = col + col_offset

        if not self.is_in_bounds(grid, new_row, new_col):
          continue
        
        if grid[new_row][new_col] == ROTTEN or grid[new_row][new_col] == EMPTY:
          continue
                
        new_neighbor = (new_row, new_col)        
        neighbors.append(new_neighbor)
      
      return neighbors 

    def get_rotting_and_fresh_oranges(self, grid):

      rotting_orange_list = []
      fresh_orange_list = []

      num_rows = len(grid)
      num_cols = len(grid[0])

      for row in range(num_rows):
        for col in range(num_cols):

          if grid[row][col] == ROTTEN:
            position = (row, col)
            rotting_orange_list.append(position)
            continue
          
          if grid[row][col] == FRESH:
            position = (row, col)
            fresh_orange_list.append(position)

      return rotting_orange_list, fresh_orange_list

    def are_fresh_oranges_remaining(self, visited, fresh_orange_list):    

      for position in fresh_orange_list:
        if position not in visited:
          return True
      
      return False 


    def get_time_for_oranges_to_rot(self, grid, rotting_orange_list, fresh_orange_list):

      queue = deque()

      time_to_rot = 0

      visited = set()

      #Have excluded cases where there are no rotting oranges
      #before this point
      for row, col in rotting_orange_list:
        position = (row, col)
        rotten_orange_tuple = position, time_to_rot
        queue.append(rotten_orange_tuple)
        visited.add(position)
      
      total_elapsed_time = 0

      while queue:

        #pop
        position, time = queue.popleft()
        row, col = position        

        #process
        total_elapsed_time = time

        #add neighbors
        neighbors = self.get_neighbors(grid, row, col)
        for neighbor in neighbors:
          if neighbor in visited:
            continue
          visited.add(neighbor)

          new_neighbor = (neighbor, time + 1)
          # print(new_neighbor)
          queue.append(new_neighbor)

      are_any_fresh_oranges_left = self.are_fresh_oranges_remaining(visited, fresh_orange_list)

      if are_any_fresh_oranges_left:
        return NOT_POSSIBLE
      
      return total_elapsed_time

    
            

    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotting_orange_list, fresh_orange_list = self.get_rotting_and_fresh_oranges(grid)        

        if len(fresh_orange_list) == 0:
          return 0    

        if len(rotting_orange_list) == 0:
          return NOT_POSSIBLE  
          
        time_elapsed = self.get_time_for_oranges_to_rot(grid, rotting_orange_list, fresh_orange_list)

        return time_elapsed 