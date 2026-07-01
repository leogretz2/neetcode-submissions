class Solution:
    # no sort, use array
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # construct map of frequencies
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        # flip keys and values (list elements for repeat frequencies)
        # freqArray is max the length of nums
        print('f',freqs)
        freqArray = [0]*(len(nums)+1)
        for element in freqs:
            elemFrequency = freqs[element]
            if isinstance(freqArray[elemFrequency], list):
                freqArray[elemFrequency] += [element]
            else:
                freqArray[elemFrequency] = [element]

        # add all frequencies to sol in reverse and return first k
        sol = []
        for idxFrequency in range(len(freqArray)):
            if isinstance(freqArray[idxFrequency], list):
                sol += [*freqArray[idxFrequency]]
            
        return sol[-k:]
