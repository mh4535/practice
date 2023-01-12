NOT_PRESENT = -1

class Solution:

    def get_first_position(self, nums, target):

        index_of_first = len(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] >= target:

                index_of_first = mid
                right = mid - 1
            
            else:

                left = mid + 1

        if index_of_first == len(nums) or nums[index_of_first] != target:
            return NOT_PRESENT
        
        return index_of_first       
        

    
    def get_last_position(self, nums, target):
        
        index_of_last = len(nums)
        left = 0
        right = len(nums) - 1
        
        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] <= target:

                index_of_last = mid
                left = mid + 1
            
            else:

                right = mid - 1
        

        if index_of_last == len(nums) or nums[index_of_last] != target:
            return NOT_PRESENT
        
        return index_of_last


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        first_position = self.get_first_position(nums, target)

        if first_position == NOT_PRESENT:
            return [NOT_PRESENT, NOT_PRESENT]

        last_position = self.get_last_position(nums, target)

        return [first_position, last_position]









