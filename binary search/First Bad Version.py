# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
NO_BAD_VERSIONS_PRESENT = -1
class Solution:
    def firstBadVersion(self, n: int) -> int:

        '''
        1 2 3 4 5
        g g g b b
        f f f t t
        '''

        left = 1
        right = n 

        boundary_index = NO_BAD_VERSIONS_PRESENT

        while left <= right:

            mid = left + (right - left) // 2

            if isBadVersion(mid):
                boundary_index = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return boundary_index  

