class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        head = 0
        tail = k - 1

        window = nums[0:k]
        res = []
        while tail < len(nums):
            maxVal = max(window)
            res.append(maxVal)

            tail += 1
            head += 1

            window = nums[head:tail+1]
    
        return res
        