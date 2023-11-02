class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_map = {"Red" : 0, "White" : 0, "Blue": 0}

        for i in range(len(nums)):
            if nums[i] == 0:
                color_map["Red"] += 1
            elif nums[i] == 1:
                color_map["White"] += 1
            else:
                color_map["Blue"] += 1

        
        itera = 0
        count = 0
        while count < color_map.get("Red"):
            nums[itera] = 0
            count += 1
            itera += 1

        count = 0
        while count < color_map.get("White"):
            nums[itera] = 1
            count += 1
            itera += 1

        count = 0
        while count < color_map.get("Blue"):
            nums[itera] = 2
            count += 1
            itera += 1
        
        
        
        