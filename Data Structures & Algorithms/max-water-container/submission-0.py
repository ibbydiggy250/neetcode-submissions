class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest = 0
        for i in range(0,len(heights)):
            for j in range(i+1, len(heights)):
                sum = (j-i)*min(heights[i], heights[j])
                if sum > greatest:
                    greatest = sum
        
        return greatest