class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        
        #left
        prefix=1
        for i in range(len(nums)):
            left[i]=prefix
            prefix*=nums[i]

        #right
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            right[i]=suffix
            suffix*=nums[i]
        
        output= [x * y for x, y in zip(left, right)]
        return output