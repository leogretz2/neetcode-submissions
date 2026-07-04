class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = len(nums) // 2 - 1 if len(nums) % 2 == 0 else len(nums) // 2
        if nums[i] > nums[i+1]:
            return nums[i+1]
        else:
            return min(self.findMin(nums[:i+1]),self.findMin(nums[i+1:]))
