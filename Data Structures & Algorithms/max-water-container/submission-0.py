class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        volume = 0

        while (left < right):
            newvol = (right - left) * min(heights[left], heights[right])
            if (newvol > volume):
                volume = newvol

            if (heights[left] <= heights[right]):
                left += 1
            elif (heights[right] <= heights[left]):
                right -= 1
        
        return volume