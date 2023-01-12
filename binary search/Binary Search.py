TARGET_NOT_FOUND = -1


class Solution:

    
    def search(self, nums: List[int], target: int) -> int:

        '''
        [-1,0,3,5,9,12]  target = 9
        '''

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid 

            if target > nums[mid]:
                low = mid + 1
                continue
            
            high = mid - 1
        
        return TARGET_NOT_FOUND



