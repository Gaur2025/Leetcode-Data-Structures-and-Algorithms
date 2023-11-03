class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # we have 2 operations --> push and pop
        # target = [1, 2, 3]  (an iterator will be required for this)
        # stack = [(1), (2), (3), 4, 5, 6, 7, 8]
        # ans = [1, 2, 3]
        # if empty => push --> check if it is target's i-th element --> if not then pop --> else push

        start = 0
        res = []

        for i in range(1, n + 1):    # since numbers are from 1 to n
            if start >= len(target):
                break

            if target[start] == i:
                start += 1
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")

        return res




