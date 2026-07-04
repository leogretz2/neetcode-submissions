class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for t_char in t:
            need[t_char] = need.get(t_char,0)+1
        required = len(need)

        window = {}
        best_start = 0
        best_length = float("inf")
        have = 0
        start = 0

        for i,c in enumerate(s):
            window[c] = window.get(c,0)+1
            if c in need and window[c] == need[c]:
                have += 1

            # while valid, try to shrink
            while have == required:
                # store current window
                if (i - start + 1) < best_length:
                    best_start = start
                    best_length = i - start + 1
                
                # pop left char
                window[s[start]] -= 1
                # break the loop
                if s[start] in need and window[s[start]] < need[s[start]]:
                    have -= 1
                start += 1


        return "" if best_length == float("inf") else s[best_start:best_start+best_length]