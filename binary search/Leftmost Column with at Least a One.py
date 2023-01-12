# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
ONE_DOES_NOT_EXIST = -1
class Solution:

    def get_leftmost_one_for_row(self, binary_matrix, row):

        '''   
        leftmost_column 

        0 , 0 , 1, 1
        f   f   t  t         '''

        num_rows, num_cols = binary_matrix.dimensions()

        leftmost_col = num_cols

        left = 0
        right = num_cols - 1

        while left <= right:

            mid = left + (right - left) // 2

            if binary_matrix.get(row, mid) == 1:
                leftmost_col = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return leftmost_col 






    def leftMostColumnWithOne(self, binary_matrix: 'BinaryMatrix') -> int:

        
        num_rows, num_cols = binary_matrix.dimensions()

        overall_leftmost_column = num_cols 

        for row in range(num_rows):
            
            this_leftmost_column = self.get_leftmost_one_for_row(binary_matrix, row)
            overall_leftmost_column = min(overall_leftmost_column, this_leftmost_column)
        
        if overall_leftmost_column == num_cols:
            return ONE_DOES_NOT_EXIST
        
        return overall_leftmost_column
            







        