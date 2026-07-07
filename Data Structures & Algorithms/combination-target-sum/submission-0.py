class TreeNode:
    def __init__(self, value):
        self.value

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0: # success
                result.append(path[:])
            if remaining < 0: # overshot - fail
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining - nums[i], path)
                path.pop()

        backtrack(0,target,[])
        return result