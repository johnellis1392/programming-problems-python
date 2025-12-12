from leetcode.reverse_bits import Solution


class Solution:
    def reverseBits(self, n: int) -> int:
        # r = 0
        # for _ in range(n.bit_length()):
        #     r = (r << 1) | (n & 0b1)
        #     n >>= 1
        # return r

        # return int(''.join(reversed(f'{n:032b}')), 2)

        # 0b11111111_11111111_11111111_11111111
        # m = 0b11111111_11111111_00000000_00000000
        # n = ((n & m) >> 16) | ((n & ~m) << 16)
        # m = 0b11111111_00000000_11111111_00000000
        # n = ((n & m) >> 8) | ((n & ~m) << 8)
        # m = 0b11110000_11110000_11110000_11110000
        # n = ((n & m) >> 4) | ((n & ~m) << 4)
        # m = 0b11001100_11001100_11001100_11001100
        # n = ((n & m) >> 2) | ((n & ~m) << 2)
        # m = 0b10101010_10101010_10101010_10101010
        # n = ((n & m) >> 1) | ((n & ~m) << 1)
        # return n

        # 0b11111111_11111111_11111111_11111111
        n = ((n & 0xFFFF0000) >> 16) | ((n & 0xFFFF) << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0xFF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0xF0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n


def test_reverse_bits():
    s = Solution()
    assert s.reverseBits(43261596) == 964176192
    assert s.reverseBits(1073741822) == 2147483644
