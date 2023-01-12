from collections import deque
    
CONNECTED = 1

class Solution:
    
    def get_neighbors(self, connections, city):
        
        num_possible_connections = len(connections)
        neighbors = []
        
        for possible_connection in range(num_possible_connections):
            if connections[city][possible_connection] == CONNECTED:
                neighbors.append(possible_connection)
        
        return neighbors
                
    
    
    def mark_connected_cities(self, connections, city, visited):
        
        queue = deque()
        queue.append(city)
        
        visited.add(city)
        
        while queue:
            
            curr_city = queue.popleft()
            
            neighbors = self.get_neighbors(connections, curr_city)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                
                queue.append(neighbor)
        
    
    def findCircleNum(self, connections: List[List[int]]) -> int:
        
        visited = set()
        
        num_connections = len(connections)
        
        num_provinces = 0
        
        for city in range(num_connections):
            if city in visited:
                continue
            self.mark_connected_cities(connections, city, visited)
            num_provinces += 1
        
        return num_provinces