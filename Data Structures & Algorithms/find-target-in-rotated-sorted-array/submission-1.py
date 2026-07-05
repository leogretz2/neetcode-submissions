class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            half = (left+right) // 2
            if nums[half] == target:
                return half

            print(nums[left], target, nums[half],nums[right])
            # check if LEFT is sorted
            if nums[left] <= nums[half]:
                # used sorted to determine half with target
                if nums[left] <= target < nums[half]:
                    right = half-1
                else:
                    left = half+1
            # RIGHT is sorted
            else:
                # used sorted to determine half with target
                if nums[half] <= target <= nums[right]:
                    left = half+1
                else:
                    right = half-1
            print('lr',left, right)

        return -1
