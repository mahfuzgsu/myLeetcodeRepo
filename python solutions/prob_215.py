class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k==1:
            return nums[0]
        
        nums= sorted(nums)
        l = len(nums)
        
        return nums[l-k]
        
        
        