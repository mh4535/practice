from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:    

    def is_in_bounds(self, matrix, row, col):

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        is_row_in_bounds = row >= 0 and row < num_rows
        is_col_in_bounds = col >= 0 and col < num_cols

        return is_row_in_bounds and is_col_in_bounds


    def get_neighbors(self, matrix, row, col):

        neighbors = []

        for row_offset, col_offset in directions:
            new_row = row_offset + row
            new_col = col_offset + col

            if not self.is_in_bounds(matrix, new_row, new_col):
                continue

            new_neighbor = (new_row, new_col)          
            
            neighbors.append(new_neighbor)
        
        return neighbors 



    def populate_queue_and_visited_with_zeros(self, matrix):

        queue = deque()
        visited = set()

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    distance = 0
                    position = (row, col)
                    visited.add(position)  
                    tuple_for_queue = (position, distance)                                      
                    queue.append(tuple_for_queue)

        return queue, visited

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:   

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        updated_matrix = [[None for _col in range(num_cols)] for _row in range(num_rows)]    

        queue, visited = self.populate_queue_and_visited_with_zeros(matrix)

        #There is at least 1 zero in matrix
        while queue:

            #pop
            position, distance = queue.popleft()
            row, col = position            

            #process
            updated_matrix[row][col] = distance

            #add neighbors
            neighbors = self.get_neighbors(matrix, row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)

                new_neighbor = (neighbor, distance + 1)
                queue.append(new_neighbor)
        
        return updated_matrix