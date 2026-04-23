class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mytable = {}
        start = 0
        maxCount = 0
        for i, char in enumerate(s):
            if char in mytable and mytable[char] >= start:
                start = mytable[char] + 1
            
            mytable[char] = i
            maxCount = max(i - start + 1, maxCount)
            
        return maxCount
            


        