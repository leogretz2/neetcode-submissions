class Solution:
    # try with O(1) extra space rather than O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(n):
            ans[-1-j] *= postfix
            postfix *= nums[-1-j]

        return ans