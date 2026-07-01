class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        sortedNums = sorted(nums)
        print('asdf',sortedNums)
        for i in range(len(sortedNums)):
            remainderToZero = 0 - sortedNums[i]
            # twoSum return could have multiple ways to get to target
            potentialSols = self.twoSum(sortedNums[:i]+sortedNums[i+1:],remainderToZero)
            print('pot', potentialSols)
            for potential in potentialSols:
                if len(potential) == 2:
                    sol.append([sortedNums[i],*potential])
        # dedupe sol by converting elements to tuples and set
        solSet = set()
        for triplet in sol:
            solSet.add(tuple(sorted(triplet)))
        solList = []
        for tupleTriplet in solSet:
            solList.append(list(tupleTriplet))

        return solList

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Construct targets with key remainder, value list of indexes where remainder located (excludes i)
        targets = {}
        pairs = []
        for i in range(len(nums)):
            targets[nums[i]] = i
        for j in range(len(nums)):
            remainder = target - nums[j]
            if remainder in targets and targets[remainder] != j:
                pairs.append([nums[j],remainder])
        return pairs