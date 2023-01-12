class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        '''
        0,1,2,1,0
        f f f t t

        0 1 2 3 4 5 6 7 8 7 5 4 3 2 0
        f f f f f f f f t t t t t t t
                             
        
       
        '''

        left = 0
        right = len(arr) - 1

        peak = 1

        while left <= right:

            mid = left + (right - left) // 2

            if arr[mid + 1] < arr[mid]:
                peak = mid
                right = mid - 1                
            else:                
                left = mid + 1
        

        return peak 