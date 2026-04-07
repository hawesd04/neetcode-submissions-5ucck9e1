class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 0
            table[num] += 1
        
        return heapq.nlargest(k, table, key=table.get)
        