class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for idx in range(len(nums)):
            targets[nums[idx]] = idx
        for idx2 in range(len(nums)):
            remainder = target - nums[idx2]
            if remainder in targets and idx2 != targets[remainder]:
                return [idx2, targets[remainder]]

