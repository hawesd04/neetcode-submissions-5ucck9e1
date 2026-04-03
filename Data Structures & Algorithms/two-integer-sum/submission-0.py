class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if (target - nums[i] in hash_table):
                return [hash_table[diff],i]
            hash_table[nums[i]] = i
        return False
