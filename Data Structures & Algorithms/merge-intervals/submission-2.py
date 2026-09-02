class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        seen = []
        for interval in intervals:
            if len(seen) == 0:
                seen.append(interval)
            elif interval[0] <= seen[-1][1]:
                seen[-1][1] = max(seen[-1][1], interval[1])
            else:
                seen.append(interval)
        res = []
        for n in seen:
            temp = []
            temp.append(min(n))
            temp.append((max(n)))
            res.append(temp)
        return res
