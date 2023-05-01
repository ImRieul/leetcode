class Solution:
    def climbStairs(self, n: int) -> int:
        fibonacci = [1, 1]

        while (len(fibonacci) < n):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

        return fibonacci[-1] + fibonacci[-2] if n > 1 else 1