class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = 0
        full_list = []
        for i in range(len(nums)):
            check = nums[i]
            for j in range(i+1, len(nums)):
                if (check + nums[j] == target):
                    full_list.append(i)
                    full_list.append(j)
        
        return full_list


        