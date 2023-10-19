class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # moving from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            # update top
            top += 1

            # moving from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            # update right 
            right -= 1

            # if row or column matrix (VERY IMP EDGE CASE)
            if not (left < right and top < bottom):
                break

            # moving from right to left
            for i in range(right - 1, left - 1, -1):   # in reverse order
                res.append(matrix[bottom - 1][i])
            # update bottom
            bottom -= 1

            # moving from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # update left
            left += 1

        return res



        