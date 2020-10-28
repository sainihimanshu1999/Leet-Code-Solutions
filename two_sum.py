class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        i = 0
        while i < len(nums):
            val = target - nums[i]
            if(val in x):
                return(x[val],i)
            x[nums[i]] = i
            i += 1