class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for num in nums:
            res ^= num  # XOR the current number with our running total
            
        return res