class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1=[]
        for i in nums:
            nums1.append(i)
        for i in nums:
            nums1.remove(i)
            if i in nums1:
                return True
        return False