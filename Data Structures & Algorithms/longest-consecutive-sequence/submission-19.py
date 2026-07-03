class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        switchSet = set(nums)
        
        seqLen, longest = 0,0

        for num in switchSet:
            if num-1 not in switchSet:
                seqLen = 0
                j = num
                while(j in switchSet):
                    seqLen += 1
                    j+=1
                longest = max(seqLen, longest)
            else:
                seqLen = 0
                continue;
        return max(seqLen, longest)