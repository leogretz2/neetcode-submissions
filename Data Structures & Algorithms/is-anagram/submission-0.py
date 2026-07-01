class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreqs, tFreqs = [0]*26, [0]*26
        for sLetter in s:
            sLetterIdx = ord(sLetter) - ord('a')
            sFreqs[sLetterIdx] += 1
        for tLetter in t:
            tLetterIdx = ord(tLetter) - ord('a')
            tFreqs[tLetterIdx] += 1
        for alphabetIdx in range(26):
            if sFreqs[alphabetIdx] != tFreqs[alphabetIdx]:
                return False
        return True
            
        