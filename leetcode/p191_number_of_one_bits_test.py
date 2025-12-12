
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


def test_hamming_weight():
    s = Solution()
    assert s.hammingWeight(11) == 3
    assert s.hammingWeight(128) == 1
    assert s.hammingWeight(2147483645) == 30
