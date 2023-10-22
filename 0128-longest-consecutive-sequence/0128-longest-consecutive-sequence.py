class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach 1: Sort the array, then in a loop find the longest consecutive sequence
        # Approach 2: To store nums inside a set. Check whether each element is start of a sequence.

        # define longest sequence
        longest = 0
        
        # Creating the set
        numSet = set(nums)

        # Iterating on the input list
        for number in nums:
            # Check whether the left element is starting of a number. If exist then it is not starting of a sequence
            if (number - 1) not in numSet:
                # defining length of the sequence 
                length = 0
                # get the length of sequence. check its right elements
                while (number + length) in numSet:
                    length += 1
            
                # update the longest variable
                longest = max(length, longest)

        # return longest
        return longest
        