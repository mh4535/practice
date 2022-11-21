from collections import defaultdict 

class Solution:

    def build_graph(self, rooms):
        
        graph = defaultdict(list)
        
        for room in range(len(rooms)):
           for neighbor in rooms[room]:
               graph[room].append(neighbor)
        
        return graph

    def mark_as_visited_rooms_that_can_be_entered(self, graph, visited, curr_room):      

        if curr_room in visited:
            return  

        visited.add(curr_room)

        if curr_room not in graph:
            return 

        neighbors = graph[curr_room]
        for neighbor in neighbors:
            if neighbor in visited:
                continue            

            self.mark_as_visited_rooms_that_can_be_entered(graph, visited, neighbor)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = self.build_graph(rooms)

        visited = set()

        initial_room = 0

        self.mark_as_visited_rooms_that_can_be_entered(graph, visited, initial_room)

        return len(visited) == len(rooms)