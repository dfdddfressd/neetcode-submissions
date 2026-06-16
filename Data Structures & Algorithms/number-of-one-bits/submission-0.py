class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        temp = str(binary)
        count = 0

        for i in range(len(temp)):
            if temp[i] == "1":
                count += 1

        return count


        

            
        