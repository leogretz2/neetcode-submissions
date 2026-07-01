class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        progressArray, product, reverseProgress, reverseProduct = (
            [0] * len(nums),
            1,
            [0] * len(nums),
            1,
        )
        for i in range(len(nums)):
            product *= nums[i]
            progressArray[i] = product
            reverseProduct *= nums[-1 - i]
            reverseProgress[-1 - i] = reverseProduct

        ans, firstPtr, secondPtr = [0] * len(nums), -1, 1
        for j in range(len(nums)):
            product = (1 if firstPtr+j < 0 else progressArray[firstPtr+j]) * (
                1 if secondPtr+j > (len(nums) - 1) else reverseProgress[secondPtr+j]
            )
            ans[j] = product
        print(progressArray, reverseProgress, ans)

        return ans
