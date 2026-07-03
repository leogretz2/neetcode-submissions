class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        small, big, switchSet = min(nums), max(nums), set(nums)
        
        seqLen, longest = 0,0
        current = small

        for i in range(len(nums)):
            if nums[i]-1 not in switchSet:
                print(nums[i])
                seqLen = 0
                j = nums[i]
                while(j in switchSet):
                    seqLen += 1
                    j+=1
                longest = seqLen if seqLen > longest else longest


                # for j in range(i, len(nums)):
                #     print(nums[j])
                #     if nums[j] in switchSet:
                #         seqLen += 1
                # longest = seqLen if seqLen > longest else longest
                # if seqLen > longest:
                #     longest = seqLen
            else:
                seqLen = 0
                continue;
        return seqLen if seqLen > longest else longest







        # while current < big+1:
        #     if current in switchSet:
        #         seqLen += 1
        #     else:
        #         if seqLen > longest:
        #             longest = seqLen
        #         seqLen = 0
            
        #     current += 1
        
        # return seqLen if seqLen > longest else longest