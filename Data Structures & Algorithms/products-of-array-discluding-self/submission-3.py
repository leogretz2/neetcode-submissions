class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive, divide total product by current for each element
        product, zeroExists = 1, False
        for num in nums:
            if num != 0:
                product *= num
            else:
                if zeroExists:
                    return [0]*len(nums)
                zeroExists = True

        for idx in range(len(nums)):
            if nums[idx] != 0 and zeroExists:
                nums[idx] = 0
            elif nums[idx] != 0:
                nums[idx] = int(product/nums[idx])
            elif nums[idx] == 0:
                nums[idx] = product

        return nums
        