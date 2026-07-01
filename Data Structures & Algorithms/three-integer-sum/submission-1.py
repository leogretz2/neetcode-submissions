class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        solList = set()
        for i in range(len(sortedNums)):
            targetZero = 0 - sortedNums[i]
            # only look forward from the anchor to prevent duplication
            sortedForward = sortedNums[i+1:]
            incrementalSolList = self.twoSumPointers(sortedForward, targetZero)
            print('sE',i, incrementalSolList)
            for incrementalSol in incrementalSolList:
                if len(incrementalSol) == 2:
                    solList.add((sortedNums[i],*incrementalSol))
        
        return [list(sol) for sol in solList]

    def twoSumPointers(self, limitedNums: List[int], target: int) -> List[List[int]]:
        ptr1, ptr2, sol = 0, len(limitedNums)-1, []
        while ptr1 < ptr2:
            total = limitedNums[ptr1] + limitedNums[ptr2]
            # print(limitedNums, target, '(',ptr1,'<',ptr2,')',total, sol)
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
        print('sol',sol)
        return sol
        