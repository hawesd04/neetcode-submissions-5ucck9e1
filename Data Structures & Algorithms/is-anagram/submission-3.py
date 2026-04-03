class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in s_table:
                s_table[char] += 1
            else:
                s_table[char] = 1

        for char in t:
            if char in t_table:
                t_table[char] += 1
            else:
                t_table[char] = 1

        if s_table == t_table:
            return True
        return False
        
