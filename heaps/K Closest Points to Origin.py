import math 

class Solution:

    def get_distance_from_origin(self, x, y):       

        return math.sqrt(x * x + y * y)


    def generate_heap(self, points):

        heap_of_points = []

        for x, y in points:

            distance_from_origin = self.get_distance_from_origin(x, y)
            new_point_with_distance_from_origin = [distance_from_origin, x, y]
            heapq.heappush(heap_of_points, new_point_with_distance_from_origin)
        
        return heap_of_points


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        k_closest_points = []

        heap_of_points = self.generate_heap(points)        
        
        for i in range(k):

            distance, x, y = heapq.heappop(heap_of_points)
            k_closest_points.append([x, y])
        
        return k_closest_points