from collections import deque
        
def is_in_bounds(row, col, image):
    
    num_rows = len(image)
    num_cols = len(image[0])
    
    row_in_bounds = row >=0 and row < num_rows
    col_in_bounds = col >= 0 and col < num_cols
    
    return row_in_bounds and col_in_bounds

class Solution:
    
    def get_neighbors(self, image, curr_row, curr_col, current_color):
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        valid_neighbors = []
        
        for direction in directions:
            row_offset, col_offset = direction
            new_row = curr_row + row_offset
            new_col = curr_col + col_offset 
            new_position = (new_row, new_col)
            
            if not is_in_bounds(new_row, new_col, image):
                continue
            
            if image[new_row][new_col] != current_color:
                continue
            
            valid_neighbors.append(new_position) 
            #print(valid_neighbors)
        
        return valid_neighbors
    
    def change_color_of_connected_pixels(self, image, start_row, start_col, replacement_color, current_color):
        
        start_position = (start_row, start_col)
        queue = deque() 
        queue.append(start_position)
        visited = set()
        visited.add(start_position)
        
        while queue:
            
            curr_row, curr_col = queue.popleft()
            
            image[curr_row][curr_col] = replacement_color
            
            neighbors = self.get_neighbors(image, curr_row, curr_col, current_color)
            
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        num_rows = len(image)
        num_cols = len(image[0])
        replacement_color = color        
        row = sr
        col = sc
        current_color = image[row][col]
        
        self.change_color_of_connected_pixels(image, row, col, replacement_color, current_color)
        
        return image