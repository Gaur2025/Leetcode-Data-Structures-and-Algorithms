class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # we can never reach if source and destination is same but time given is 1, as we are already at the destination
        if (sx == fx and sy == fy and t == 1):
            return False

        
        # we can reach at destination if both the absolute horizontal and vertical distance is lesser or equals to t
        if (abs(sx - fx) <= t and abs(sy - fy) <= t):
            return True

        # in all other cases
        return False