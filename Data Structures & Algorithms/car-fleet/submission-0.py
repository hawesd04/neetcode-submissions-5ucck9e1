class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # list comprehension, array of pairs in python (list of 'position: speed')
        # merges the two lists
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # iterate by position and speed in reverse sorted order, ::-1 to reverse, pos first so sort by pos
        for p, s in sorted(pair)[::-1]: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        