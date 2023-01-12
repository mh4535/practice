class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
                3, 4, 5, 1, 2
                f  f  f  t  t


                6,7,0,1,2,3 4, 5
                f f t t t t t  t
                
        '''

        # if len(nums) == 1 or (nums[0] < nums[len(nums) - 1]):
        #     return nums[0]

        left = 0
        right = len(nums) - 1

        pivot = 0

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] < nums[0]:
                pivot = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[pivot]


