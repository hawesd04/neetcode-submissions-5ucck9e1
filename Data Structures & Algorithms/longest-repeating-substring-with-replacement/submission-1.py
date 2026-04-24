class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        start = 0
        res = 0

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1

            windowlen = i - start + 1
            maxCnt = max(hashmap.values())

            if ((windowlen - maxCnt) <= k):
                res = windowlen
            else:
                hashmap[s[start]] -= 1
                start += 1


        return res 

        