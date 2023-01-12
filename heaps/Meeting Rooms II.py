START_TIME = 0
END_TIME = 1

class Solution:

    '''
    2,10     3,5    4,9    6,10              

      
        4     9
            6    10
    2            10
      
      
            6    10
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda x: x[START_TIME])          
        last_finish_time = 0
        num_rooms_needed = 1
        heap_of_intervals = []       
        
        for interval in intervals:

            curr_interval_start_time, curr_interval_end_time = interval

            if not heap_of_intervals:
                heapq.heappush(heap_of_intervals, curr_interval_end_time)
                continue 

            earliest_end_time = heap_of_intervals[0]

            while curr_interval_start_time >= earliest_end_time and heap_of_intervals:

                heapq.heappop(heap_of_intervals)

                if heap_of_intervals:
                    earliest_end_time = heap_of_intervals[0]

            heapq.heappush(heap_of_intervals, curr_interval_end_time)
            num_rooms_needed = max(num_rooms_needed, len(heap_of_intervals))

        return num_rooms_needed







                

        


