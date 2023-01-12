from collections import deque

GATE = 0
OBSTACLE = -1
EMPTY_ROOM = 2147483647

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:

    def is_in_bounds(self, rooms, row, col):

        num_rows = len(rooms)
        num_cols = len(rooms[0])

        row_is_in_bounds = row >= 0 and row < num_rows
        col_is_in_bounds = col >= 0 and col < num_cols

        return row_is_in_bounds and col_is_in_bounds

    def get_neighbors(self, rooms, row, col):

        neighbors = []
        
        for row_offset, col_offset in directions:

            new_row = row_offset + row
            new_col = col_offset + col
            
            if not self.is_in_bounds(rooms, new_row, new_col):
                continue
            
            if rooms[new_row][new_col] == OBSTACLE:
                continue
            
            new_neighbor = (new_row, new_col)

            neighbors.append(new_neighbor)
        
        return neighbors
    
    def populate_queue_and_visited_with_gates(self, rooms):

        num_rows = len(rooms)
        num_cols = len(rooms[0])

        queue = deque()

        visited = set()

        for row in range(num_rows):
            for col in range(num_cols):

                if rooms[row][col] == GATE:
                    new_gate = (row, col)
                    distance = 0
                    gate_tuple = (new_gate, distance)
                    queue.append(gate_tuple)
                    visited.add(new_gate)

        return queue, visited 

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()

        queue, visited = self.populate_queue_and_visited_with_gates(rooms)

        if len(queue) == 0:
            return
        
        while queue:

            #pop
            position, distance = queue.popleft()
            row, col = position
            
            #process
            rooms[row][col] = distance           

            #add neighbors
            neighbors = self.get_neighbors(rooms, row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)

                new_neighbor = (neighbor, distance + 1)
                queue.append(new_neighbor)