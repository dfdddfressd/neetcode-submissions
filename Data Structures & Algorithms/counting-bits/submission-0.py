class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(0, n+1):
            ones = 0
            ibin = bin(i)
            while i:
                ones += i & 1
                i = i>>1
            bits.append(ones)
        return(bits)