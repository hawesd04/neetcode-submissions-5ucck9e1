class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "!empty"
        
        combine = ""
        for i in range(len(strs)):
            if (i != (len(strs) - 1)):
                combine += (strs[i] + "#, ")
            else:
                combine += (strs[i])
        return combine

    def decode(self, s: str) -> List[str]:
        if s == "!empty":
            return []
        return s.split("#, ")

