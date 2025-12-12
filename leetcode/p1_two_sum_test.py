from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, n in enumerate(nums):
            if target-n in dp:
                return [dp[target-n], i]
            dp[n] = i
        raise RuntimeError("Could not find solution")


def test_two_sum():
    s = Solution()
    assert s.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert s.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert s.twoSum(nums=[3, 3], target=6) == [0, 1]
