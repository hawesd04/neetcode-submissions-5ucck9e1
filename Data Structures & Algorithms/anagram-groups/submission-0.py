class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_table = {}
        count = 0

        for word in strs:
            sort = "".join(sorted(word))
            if sort not in my_table.keys():
                my_table[sort] = []
            my_table[sort].append(word)
            
        return list(my_table.values())