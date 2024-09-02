class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        temp = 0

        for _ in range(32):

            temp = (temp << 1) + (n & 1)
            n >>= 1

        return temp