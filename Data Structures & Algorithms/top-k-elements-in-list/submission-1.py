import statistics
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = []
        lists = nums
        for i in range(0,k):
            topk = statistics.mode(lists)
            lists = [item for item in lists if item != topk]
            top.append(topk)
        
        return top

            
        