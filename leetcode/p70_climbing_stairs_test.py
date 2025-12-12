
class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 <= n and n <= 2:
            return n
        a, b = 1, 2
        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b

    def climbStairs2(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]


def test_climb_stairs():
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
