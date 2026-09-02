class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # minimize the height difference
        # maximize the distance between heights
        maxArea = 0
        l, r = 0, len(heights) - 1
        while r > l:
            distance = r - l
            heightDiff = min(heights[r], heights[l])
            area = distance * heightDiff
            maxArea = max(maxArea, area)
            if heights[r] >= heights[l]:
                l = l+1
            else:
                r = r-1
        return maxArea