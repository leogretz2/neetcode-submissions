class Solution:
    # increase start to place after duplicate
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, currentLength = 0,0
        substringHashSet = set()
        start = 0
        for i in range(len(s)):
            # print(start, s[i], substringHashSet, maxLength, currentLength)
            if s[i] in substringHashSet:
                maxLength = max(len(substringHashSet), maxLength)
                # currentLength = 0
                print('hit',start,i,s[i])
                # for j in range(start,i):
                while s[i] in substringHashSet:
                    substringHashSet.remove(s[start])    
                    start+=1
                # substringHashSet.remove(s[start])
                substringHashSet.add(s[i])
                # start = i-start+1
            else:
                substringHashSet.add(s[i])
                currentLength = len(substringHashSet)
        return max(currentLength,maxLength)