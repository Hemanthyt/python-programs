class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                print(stack)
        return len(stack)
s = Solution()
print(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))