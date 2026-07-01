class Solution:
    # brute force O(n^2)
    def maxArea(self, heights: List[int]) -> int:
        max_container_area = 0
        for left in range(len(heights)-1):
            right = left+1
            while right < len(heights):
                area = min(heights[left], heights[right]) * (right-left)
                right += 1
                if area > max_container_area:
                    max_container_area = area
        return max_container_area
