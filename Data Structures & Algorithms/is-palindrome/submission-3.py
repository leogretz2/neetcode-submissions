class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pre-processing
        # extra O(n) space
        processedS = ""
        for i in range(len(s)):
            c = s[i]
            if c.isalnum():
                processedS += c
        processedS = processedS.lower()

        if not processedS:
            return True
        'fivef'
        for i in range(len(processedS)//2+1):
            if processedS[i] != processedS[-1-i]:
                return False

        # print(processedS)

        return True
        