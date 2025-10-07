class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        # Split road into segments separated by '.'
        segmentsList = []
        idx = 1
        startIdx = 1
        road_len = len(road)
        while idx <= road_len + 1:
            if idx > road_len or road[idx - 1] == '.':
                # substring from startIdx to idx-1 (both 1-based)
                segment = road[startIdx - 1 : idx - 1]
                segmentsList.append(segment)
                startIdx = idx + 1
            idx += 1

        def segmentLengthAsc(seg: str) -> int:
            return len(seg)

        sortedSegments = sorted(segmentsList, key=segmentLengthAsc)

        totalFixed = 0
        # Use 0-based indexing for Python; pseudocode uses 1-based indexing
        for currentSegment in sortedSegments:
            segmentLen = len(currentSegment)
            if segmentLen != 0:
                repairCost = segmentLen + 1
                if repairCost <= budget:
                    totalFixed += segmentLen
                    budget -= repairCost
                else:
                    # tryReduceAndFix modifies the passed variables in pseudocode,
                    # in python we need a helper function that returns new values
                    n, c, b, fixed = segmentLen, repairCost, budget, totalFixed
                    n, c, b, fixed = self.tryReduceAndFix(n, c, b, fixed)
                    totalFixed, budget = fixed, b
        return totalFixed

    def tryReduceAndFix(self, n: int, c: int, b: int, fixed: int):
        while n > 0 and b > 0:
            c = n + 1
            if b >= c:
                fixed += n
                b -= c
                break
            n -= 1
        return n, c, b, fixed