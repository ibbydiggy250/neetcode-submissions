class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sub = [nums[i], nums[j], nums[k]]
                        sub.sort()
                        if sub not in ans:
                            ans.append(sub)
        return ans
