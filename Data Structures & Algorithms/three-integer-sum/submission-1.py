class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num, in enumerate(nums):
            if (i > 0 and num == nums[i-1]):
                continue

            head = i + 1
            tail = len(nums) - 1

            while (head < tail):
                threeSum = num + nums[head] + nums[tail]
                if threeSum > 0:
                    tail -= 1
                elif threeSum < 0:
                    head += 1
                else:
                    res.append([num, nums[head], nums[tail]])
                    head += 1
                    while (nums[head] == nums[head - 1] and head < tail):
                        head += 1
        
        return res
