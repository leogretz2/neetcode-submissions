class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        small, big, switchSet = min(nums), max(nums), set(nums)
        
        seqLen, longest = 0,0
        current = small

        for i in range(len(nums)):
            if nums[i]-1 not in switchSet:
                seqLen = 0
                j = nums[i]
                while(j in switchSet):
                    seqLen += 1
                    j+=1
                longest = max(seqLen, longest)
            else:
                seqLen = 0
                continue;
        return max(seqLen, longest)