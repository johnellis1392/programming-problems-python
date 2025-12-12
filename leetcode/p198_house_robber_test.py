from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], nums[1]
        b = max(a, b)
        for n in nums[2:]:
            a, b = b, max(a + n, b)
        return max(a, b)


def test_rob():
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([2, 1]) == 2
    assert s.rob([2, 1, 1, 2]) == 4
