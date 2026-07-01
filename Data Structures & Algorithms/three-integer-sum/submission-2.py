class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        solList = []
        for i in range(len(sortedNums)):
            if sortedNums[i] > 0: # ?
                break;
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue; # skip repeated anchors
            targetZero = 0 - sortedNums[i]
            # only look forward from the anchor to prevent duplication
            sortedForward = sortedNums[i+1:]
            incrementalSolList = self.twoSumPointers(sortedForward, targetZero)
            for incrementalSol in incrementalSolList:
                if len(incrementalSol) == 2:
                    solList.append([sortedNums[i],*incrementalSol])
        
        return solList

    def twoSumPointers(self, limitedNums: List[int], target: int) -> List[List[int]]:
        ptr1, ptr2, sol = 0, len(limitedNums)-1, []
        while ptr1 < ptr2:
            total = limitedNums[ptr1] + limitedNums[ptr2]
            if total < target:
                ptr1 += 1
            elif total > target:
                ptr2 -= 1
            else:
                sol.append([limitedNums[ptr1], limitedNums[ptr2]])
                ptr1 += 1
                ptr2 -= 1
                while ptr1 < ptr2 and limitedNums[ptr1] == limitedNums[ptr1-1]:
                    ptr1 += 1
        return sol
        