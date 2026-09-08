class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        greatest = 1
        if len(nums) == 0:
            count = 0
            return count
        for i in range(0,len(nums)-1) :
            if nums[i+1] == nums[i]+1:
                count += 1
                if count > greatest:
                    greatest = count
            elif nums[i+1] == nums[i]:
                count = count
            else:
                count = 1
        return greatest
    


        