class Solution:
    # increase start to place after duplicate
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, currentLength = 0,0
        substringDict = {}
        start = 0
        for i in range(len(s)):
            # print(start, s[i], substringDict, maxLength, currentLength)
            if s[i] in substringDict and substringDict[s[i]] >= start:
                # maxLength = max(len(substringDict), maxLength)

                # currentLength = 0
                print('hit',start,i,s[i])
                start=substringDict[s[i]]+1

            # add to substringDict and update start regardless
            substringDict[s[i]]=i
            maxLength = max(i-start+1, maxLength)
            # print('aft',start, s[i], substringDict, maxLength, currentLength)

                # start = i-start+1
            
            # else:
            #     substringDict[s[i]]=i
            #     currentLength = len(substringDict)
        # return max(currentLength,maxLength)
        return maxLength