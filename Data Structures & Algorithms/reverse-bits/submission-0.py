class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0

        for i in range(31, -1, -1):
            reverse = reverse << 1
            reverse = (n & 1) + reverse
            n = n >> 1
            print(reverse)
        
        return(reverse)

            