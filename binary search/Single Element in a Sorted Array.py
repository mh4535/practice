

class Solution:

    def is_odd(self, index):

        return index % 2 != 0

    def singleNonDuplicate(self, nums: List[int]) -> int:

         
        left = 0
        right = len(nums) - 1

        unpaired_element_index = -1

        while left < right:

            mid = left + (right - left) // 2

            #Start at even-numbered index
            if self.is_odd(mid):
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                unpaired_element_index = mid
                right = mid
        
        return nums[unpaired_element_index]

