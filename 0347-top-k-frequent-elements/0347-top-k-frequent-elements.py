class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creating a hasmap to store count of each value in nums
        count_hmp = {}
        # we want to store list of value for each count
        freq = [[] for _ in range(len(nums) + 1)]

        # getting count of each value from list and storing it into the hashmap
        for num in nums:
            count_hmp[num] = 1 + count_hmp.get(num, 0)

        # till here we have count of each value in the list

        # Now we want to fill out freq list containing lists of values with a specfic count.
        for value, count in count_hmp.items():
            freq[count].append(value)

        
        # Now we want to return k most frequent element. So, we need to iterate reversely on freq and get value upto k count
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # we want to stop when we get k element
                if len(res) == k:
                    return res
