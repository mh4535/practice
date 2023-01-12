class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        '''
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        f f f t t t t t t t   t  t  t  t  t  t

        1 2 3 4 5 6 7 8 9 10 11 12 13 14 
        f f f f t t t t t t   t  t  t  t  
                m
        '''

        left = 1
        right = num
        possible_square_root = 1

        while left <= right:

            mid = left + (right - left) // 2

            if mid * mid >= num:
                possible_square_root = mid
                right = mid - 1

            else:
                left = mid + 1

        is_square_perfect = possible_square_root * possible_square_root == num

        return is_square_perfect

