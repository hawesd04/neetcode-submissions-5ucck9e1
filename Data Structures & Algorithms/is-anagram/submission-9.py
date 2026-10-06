class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}

        if (len(s) != len(t)):
            return False

        for char in s:
            if char not in s_table:
                s_table[char] = 1
            else:
                s_table[char] += 1

        for char in t:
            if char not in t_table:
                t_table[char] = 1
            else:
                t_table[char] += 1
        
        return (s_table == t_table)