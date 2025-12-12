from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # for i in range(len(nums)-2):
        #   for j in range(i+1, len(nums)-1):
        #     for k in range(j+1, len(nums)):
        #       if nums[i] + nums[j] + nums[k] == 0:
        #         res.add(sorted([nums[i], nums[j], nums[k]]))
        for i in range(len(nums)-1):
            target = -nums[i]
            dp = {}
            for j in range(i+1, len(nums)):
                if target-nums[j] in dp:
                    res.append([nums[i], nums[j], nums[dp[target-nums[j]]]])
                else:
                    dp[nums[j]] = j
        return res


def test_three_sum():
    s = Solution()
    # assert sorted(sorted(a) for a in s.threeSum([-1,0,1,2,-1,-4])) == sorted(sorted(a) for a in [[-1,-1,2],[-1,0,1]])
    # assert s.threeSum([0,1,1]) == []
    # assert s.threeSum([0,0,0]) == [[0,0,0]]
    pass
