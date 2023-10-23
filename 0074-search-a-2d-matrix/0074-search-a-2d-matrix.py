class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Binary search approach.
            1. first we need to find the row in which our tartget may be present.
            2. if that row is found, then find the target in that specific row.
            3. above searches are done using binary search algorithm
        """

        nrows, ncols = len(matrix), len(matrix[0])

        # Find the row in which the target might be present. TC = O(log(nrows))
        top, bottom = 0, nrows - 1
        while top <= bottom:
            midRow = (top + bottom) // 2

            # if target is greater than the last element of row, it means target is preent in next rows
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:   # if target is less than first element of row, then we shoud search rows before midrow
                bottom = midRow - 1
            else:                              # we found the row in which target might be present
                break

        # if row not found
        if not top <= bottom:
            return False

        # Now, till this point we have a row in which target may be present. TC = O(log(ncols))
        possibleRow = (top + bottom) //2
        left, right = 0, ncols - 1
        while left <= right:
            mid = (left + right) // 2

            if target > matrix[possibleRow][mid]:
                left = mid + 1
            elif target < matrix[possibleRow][mid]:
                right = mid - 1
            else:
                # target found
                return True

        # if target not found in the possibleRow as well
        return False


# TC = O(nrows) + O(ncols) = O(nrows*ncols)
# SC = O(1)




        