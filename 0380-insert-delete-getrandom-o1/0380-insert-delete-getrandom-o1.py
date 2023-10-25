import random

class RandomizedSet:

    def __init__(self):
        self.store = set()       # this is an hashset which will contain the values
        

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        
        # if element not present we will add this element into the hashset
        self.store.add(val)    # This is O(1) process
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.store:    # O(1)
            self.store.discard(val)
            return True

        # if the element is not present
        return False  
        

    def getRandom(self) -> int:
        temp = tuple(self.store)
        # use random.choice() function
        return random.choice(temp)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()