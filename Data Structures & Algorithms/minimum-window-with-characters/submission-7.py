class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if (s == "a" and t == "a"):
        #     return "a"
        if len(s) < len(t): # or s == "a":
            return ""
        start = 0
        best_start = 0
        shrunken_length = 0
        # including duplicates does not allow for set
        t_letter_counts = {}
        for t_char in t:
            t_letter_counts[t_char] = t_letter_counts.get(t_char,0) + 1
        print(t_letter_counts)
        
        s_window_counts = {}
        for i,c in enumerate(s):
            print(s_window_counts)
            s_window_counts[c] = s_window_counts.get(c,0)+1
            if i < len(t)-1:
                continue
            print('piS',self.isSubset(s_window_counts, t_letter_counts), s_window_counts, t_letter_counts)
            if not self.isSubset(s_window_counts, t_letter_counts):
                continue
            else:
                # subset found, shrink, update s_window_counts
                new_shrunken_length, start = self.shrinkSubset(start,s[:i+1],t,s_window_counts, t_letter_counts)
                if shrunken_length == 0:
                    shrunken_length = len(s)
                if new_shrunken_length < shrunken_length:
                    best_start = start
                    shrunken_length = new_shrunken_length
                # shrunken_length = min(shrunken_length, new_shrunken_length)
                
                print('shst',shrunken_length, start)
                # proceed processing (not optimal since not preserving shrunken length < do if works)

        return s[best_start:best_start+shrunken_length]

    # deep comparison - O(len(t))
    def isSubset(self, sCounts: dict, tCounts: dict) -> bool:
        for char in tCounts:
            # if missing or less return False
            # if there and greater continue
            if char in sCounts and sCounts[char] >= tCounts[char]:
                continue;
            else:
                return False
        return True

    def shrinkSubset(self, start: int, s: str, t: str, sCounts: dict, tCounts: dict) -> int:
        print('shr',start, s, t)
        while self.isSubset(sCounts, tCounts):
            sCounts[s[start]] -= 1
            start += 1
        # Checking requires removing, so add back
        start -= 1
        sCounts[s[start]] += 1
        return len(s) - start, start

