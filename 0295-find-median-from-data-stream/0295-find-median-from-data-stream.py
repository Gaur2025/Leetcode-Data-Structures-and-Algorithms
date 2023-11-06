class MedianFinder:

    def __init__(self):
        self.store = []
        

    def addNum(self, num: int) -> None:
        self.store.append(num)

        

    def findMedian(self) -> float:
        # for finding median we need to sort the list, and then return the median
        l = len(self.store)
        if l == 0:
            return 0

        if l == 1:
            return self.store[0]

        self.store.sort()

        if l % 2 == 0:
            first = (l // 2) - 1
            second = first + 1
            s = self.store[first] + self.store[second]
            return s/2
        else:
            return self.store[(l // 2)]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()