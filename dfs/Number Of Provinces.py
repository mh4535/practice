CONNECTED = 1

class Solution:

    def get_neighbors(self, grid, city):

        other_cities = len(grid[0])

        neighbors = []
        
        for other_city in range(other_cities):

            if city == other_city:
                continue

            if grid[city][other_city] != CONNECTED:
                continue

            neighbors.append(other_city)        
        
        return neighbors 

    def mark_connected_cities(self, grid, visited, city):
        
        if city in visited:
            return 
        
        visited.add(city)

        neighbors = self.get_neighbors(grid, city)
        for neighbor in neighbors:            
            if neighbor in visited:
                continue
            
            self.mark_connected_cities(grid, visited, neighbor)



    def findCircleNum(self, grid: List[List[int]]) -> int:

        num_rows, num_cols = len(grid), len(grid[0])

        num_provinces = 0

        visited = set()

        for city in range(num_rows):
            for other_city in range(num_cols):
                if grid[city][other_city] == CONNECTED and city not in visited:
                    num_provinces += 1
                    self.mark_connected_cities(grid, visited, city)
        
        return num_provinces