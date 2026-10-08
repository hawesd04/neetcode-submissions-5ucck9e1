class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for word in strs:
            sort = "".join(sorted(word))
            if sort not in hash_table:
                hash_table[sort] = [word]
            else:
                hash_table[sort].append(word)
		
        return list(hash_table.values())