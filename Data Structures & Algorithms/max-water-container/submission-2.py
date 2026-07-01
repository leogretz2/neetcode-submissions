class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, max_container_area = 0, len(heights)-1, 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if max_container_area < area:
                max_container_area = area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_container_area