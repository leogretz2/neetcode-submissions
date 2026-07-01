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
        # add 0s to array until index elemFrequency
        print('f',freqs)
        freqArray = []
        for element in freqs:
            elemFrequency = freqs[element]
            if (len(freqArray)-1 < elemFrequency):
                freqArray += [0]*(elemFrequency-len(freqArray)+1)
            print('in',freqArray)
            if isinstance(freqArray[elemFrequency], list):
                freqArray[elemFrequency] += [element]
            else:
                freqArray[elemFrequency] = [element]
        
        print(freqArray)

        # add all frequencies to sol in reverse and return first k
        sol = []
        for idxFrequency in range(len(freqArray)):
            if isinstance(freqArray[-1-idxFrequency], list):
                # print(*frequencyList, [*frequencyList])
                sol += [*freqArray[-1-idxFrequency]]
            
        return sol[:k]
