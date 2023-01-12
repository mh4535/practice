from collections import deque

CANNOT_UNLOCK = -1
START = "0000"
NINE_STRING = '9'
ZERO_STRING = '0'

class Solution:

    def get_str_with_replacement_char(self, combination, i, char_moved_up):

        '''8030  8020'''
        before_change = combination[: i]

        after_change = combination[i + 1: len(combination)]

        return before_change + char_moved_up + after_change

    def get_down(self, char):

        if char == ZERO_STRING:
            return NINE_STRING
        
        char_as_num = int(char)
        char_as_num -= 1

        return str(char_as_num)

    def get_up(self, char):

        if char == NINE_STRING:
            return ZERO_STRING
        
        char_as_num = int(char)
        char_as_num += 1

        return str(char_as_num)

    def get_neighbors(self, combination):

        neighbors = []

        for i in range(len(combination)):
            char = combination[i]

            char_moved_up = self.get_up(char)
            char_moved_down = self.get_down(char)

            new_neighbor = self.get_str_with_replacement_char(combination, i, char_moved_up)
            neighbors.append(new_neighbor)

            new_neighbor = self.get_str_with_replacement_char(combination, i, char_moved_down)
            neighbors.append(new_neighbor)

        return neighbors

    def get_min_num_steps_to_unlock(self, dead_ends, START, target):

        queue = deque()
        num_steps = 0
        initial_tuple = (START, num_steps)
        queue.append(initial_tuple)

        visited = set()
        visited.add(START)

        while queue:

            combination, num_steps = queue.popleft()

            if combination == target:
                return num_steps
            
            neighbors = self.get_neighbors(combination)
            for neighbor in neighbors:
                if neighbor in visited or neighbor in dead_ends:
                    continue
                visited.add(neighbor)

                new_neighbor = (neighbor, num_steps + 1)
                queue.append(new_neighbor)
        

        return CANNOT_UNLOCK



    def openLock(self, deadends: List[str], target: str) -> int:

        dead_ends = set(deadends)
        
        min_num_steps_to_unlock = 0

        if START in dead_ends or target in dead_ends:
            return CANNOT_UNLOCK
        
        min_num_steps_to_unlock = self.get_min_num_steps_to_unlock(dead_ends, START, target)

        return min_num_steps_to_unlock