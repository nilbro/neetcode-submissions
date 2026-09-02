class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # minimize the height difference
        # maximize the distance between heights
        maxArea = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                distance = j - i 
                heightDiff = min(heights[i],heights[j])
                area = distance * heightDiff
                maxArea = max(area, maxArea)
        return maxArea