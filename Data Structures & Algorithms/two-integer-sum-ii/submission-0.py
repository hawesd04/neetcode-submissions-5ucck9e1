class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while (head < tail):
            added = numbers[head] + numbers[tail]

            if (added == target):
                return [head + 1, tail + 1]
            elif (added > target):
                tail -= 1
            else:
                head += 1
