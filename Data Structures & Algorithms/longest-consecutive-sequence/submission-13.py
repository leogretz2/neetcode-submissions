class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        small, big, switchSet = min(nums), max(nums), set(nums)
        
        seqLen, longest = 0,0
        current = small

        print(switchSet)

        while current < big+1:
            # print(current, big, seqLen, longest)
            if current in switchSet:
                seqLen += 1
            else:
                if seqLen > longest:
                    longest = seqLen
                seqLen = 0
            
            current += 1
        
        return seqLen if seqLen > longest else longest