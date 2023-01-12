from collections import defaultdict

class Solution:

    def populate_map(self, nums):

        map = defaultdict(int)
        num_set = set()

        for num in nums:

            num_set.add(num)
            map[num] += 1
        
        return map
    
    # def populate_heap(self, nums):

    #     num_heap = []
    #     num_to_frequency_map, num_set = self.populate_map_and_set(nums)

    #     for num in num_set:
    #         frequency = -1 * num_to_frequency_map[num]
    #         heapq.heappush(num_heap, [frequency, num])

    #     return num_heap


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        3,3,3,3,1,1,2
        1,1,2,3,3,3,3,4        
        '''        
        
        k_most_frequent_elements = []
        num_heap = []
        num_to_frequency_map = self.populate_map(nums)
        num_set = set(nums)

        for num in num_set:

            heap_element = (num_to_frequency_map[num], num)
            heapq.heappush(num_heap, heap_element)

            if len(num_heap) > k:
                heapq.heappop(num_heap)
            
        for i in range(k):

            frequency, num = heapq.heappop(num_heap)
            k_most_frequent_elements.append(num)
        
        return k_most_frequent_elements




        
        
        
        return k_most_frequent_elements



