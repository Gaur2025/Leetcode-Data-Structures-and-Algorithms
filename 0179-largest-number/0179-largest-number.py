class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        This function returns the largest number of rearranging the list numbers.
        """
        # mergeSort function
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
        
            mid = len(nums) // 2
            
            leftPart = mergeSort(nums[:mid])
            rightPart = mergeSort(nums[mid:])

            return merge(leftPart, rightPart)

        # merge of two sub lists
        def merge(leftPart, rightPart):
            result  = []
            l, r = 0, 0

            while (l < len(leftPart) and r < len(rightPart)):
                # "9" "49" ⇒ 949 > 499
                if int(str(leftPart[l]) + str(rightPart[r])) > int(str(rightPart[r]) + str(leftPart[l])):
                    result.append(leftPart[l])
                    l += 1
                else: 
                    result.append(rightPart[r])
                    r += 1

            # if elements remained in leftPart
            while l < len(leftPart):
                result.append(leftPart[l])
                l += 1

            # if elements remained in rightPart
            while r < len(rightPart):
                result.append(rightPart[r])
                r += 1

            return result

        
        # final results
        sorted_nums = mergeSort(nums)
        
        ans = str(int("".join(map(str, sorted_nums))))
        return ans

        