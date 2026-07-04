class Solution:
    # trivial O(n)
    def findMin(self, nums: List[int]) -> int:
        for i,c in enumerate(nums):
            if i+1 == len(nums):
                return nums[0]
            if nums[i] > nums[i+1]:
                return nums[i + 1]
        
        # return nums[0]