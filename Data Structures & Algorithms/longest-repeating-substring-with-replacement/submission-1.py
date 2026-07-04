class Solution:
    # maintain most_frequent_char, derive total_others from window_length
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        window_counts = {}
        k_left = k
        # total_others = 0
        most_frequent_char = ''
        current_length, longest_seq = 0,0
        for i,c in enumerate(s):
            print(window_counts, most_frequent_char, current_length, start)
            if c in window_counts:
                window_counts[c] += 1
                if c != most_frequent_char and window_counts[c] > window_counts[most_frequent_char]:
                    most_frequent_char = c
            else:
                window_counts[c] = 1
                if len(window_counts) == 1:
                    most_frequent_char = c
            current_length += 1
            if current_length - window_counts[most_frequent_char] > k:
                window_counts[s[start]] -= 1
                start+=1
                # current_length is window_length
                current_length -= 1

        return max(current_length, longest_seq)