class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        doubles = set()
        for i in range(len(nums)):
            if nums[i] not in doubles:
                doubles.add(nums[i])
            else:
                doubles.remove(nums[i])

        return doubles.pop()
                

            
            
        