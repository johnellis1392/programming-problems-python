import math
from typing import List, Optional


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins = list(reversed(sorted(coins)))

    #     def walk(total: int) -> Optional[int]:
    #         if total == 0:
    #             return 0
    #         elif total < 0:
    #             return None
    #         for c in coins:
    #             r = walk(total - c)
    #             if r != None:
    #                 return r + 1
    #         return None

    #     r = walk(amount)
    #     if r == None:
    #         return -1
    #     return r

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i - c < 0:
                    pass
                else:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[amount] == math.inf:
            return -1
        return dp[amount]


def test_coin_change():
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([186, 419, 83, 408], 6249) == 20
