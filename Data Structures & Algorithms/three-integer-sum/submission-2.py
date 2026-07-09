class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        for i,v in enumerate(nums):
            if i>0 and nums[i-1]==v:
                continue
        
            l,r=i+1,len(nums)-1

            while l<r:
                threesum=v+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1 # why cant we do r-=1; and why do we have this when we alr skipped over duplicates in the first if statement
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

        return res

