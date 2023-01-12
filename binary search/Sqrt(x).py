class Solution:
    def mySqrt(self, target: int) -> int:

        '''
            1 2 3 4 5 6 7 8 9 
            t t t f f f f f f
                  r
                m l
            
            1 2 3 4 5 6 7 8   
            t t f f f f f f
                  m

        '''

        left = 1
        right = target

        square_root = 0

        while left <= right:

            mid = left + (right - left) // 2

            if mid * mid > target:
                right = mid - 1
            
            else: 
                square_root = mid
                left = mid + 1
        
        return square_root
