DEFAULT_POSITION = 0

class Solution:

    def mid_larger_than_target(self, mid_element, target):

        return ord(mid_element) > ord(target)

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        '''
        "c","f","j"   target = "a"
         t   t   t

         a, b, c   target = a
         f  t  t

         c, f, j target = c
         f  t  t

         a b c d e f g h   target = f
         f f f f f f t t
                     m
        '''

        left = 0
        right = len(letters) - 1
        smallest_greater_than_target = DEFAULT_POSITION

        while left <= right:

            mid = left + (right - left) // 2

            if self.mid_larger_than_target(letters[mid], target):
                smallest_greater_than_target = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return letters[smallest_greater_than_target]










