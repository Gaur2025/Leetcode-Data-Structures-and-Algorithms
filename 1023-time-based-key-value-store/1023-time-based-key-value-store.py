class TimeMap(object):

    def __init__(self):
        # we can create a hashmap to store key and values associated with it
        self.store = {}    # key: list of [value, timestamp]
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # check if key is present in the store
        if key not in self.store:
            # if not present create a list of [value, timestamp] for it
            self.store[key] = []
        # now fill values in it
        self.store[key].append([value, timestamp])


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # if not found we need to return empty string
        res = ""

        # for the key we should get the values from the hashmap
        values = self.store.get(key, [])        # empty list will be returned if no value found for key

        # now we know timestamp is strictly increasing, we can use binary search to get the most recent timestamp.
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            # most recent timestamp will be always present on the left part of the search results.
            if values[mid][1] <= timestamp:
                res = values[mid][0]         # values[mid][0] --> this will return the timestamp
                # now chcek in the other half
                left = mid + 1 
            else:
                # check in the left half
                right = mid - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)