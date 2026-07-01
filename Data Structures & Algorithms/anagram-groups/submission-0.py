class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        existingAnagrams = {}
        for word in strs:
            wordFreqs = self.wordFrequencies(word)
            print(wordFreqs)
            if wordFreqs in existingAnagrams:
                # can't use dict as key
                existingAnagrams[wordFreqs] += [word]
            else:
                existingAnagrams[wordFreqs] = [word]
        print(existingAnagrams.values())
        return list(existingAnagrams.values())
        
    def wordFrequencies(self, word):
        freqs = [0]*26
        for letter in word:
            idx = ord(letter)-ord('a')
            # if letter in freqs:
            freqs[idx] += 1
            # else:
                # freqs[letter] = 1
        # fail
        # return list(dict(sorted(freqs.items())).items())
        return tuple(freqs)