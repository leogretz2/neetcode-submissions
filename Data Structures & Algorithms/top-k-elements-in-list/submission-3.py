class Solution:
    # map (sort it - nlogn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            if i in freqs:
                freqs[i] +=1
            else:
                freqs[i] = 1
        
        freqFlipped = {}
        for key in freqs:
            if freqs[key] in freqFlipped:
                freqFlipped[freqs[key]] += [key]
            else:
                freqFlipped[freqs[key]] = [key]

        sol = []
        sortedFreqsFlipped = sorted(freqFlipped.items())
        print(freqs, freqFlipped, sortedFreqsFlipped, sortedFreqsFlipped[-1])
        for j in range(k):
            if len(sol) < k:
                sol += [*sortedFreqsFlipped[-1-j][1][:(k-len(sol))]]

        return sol