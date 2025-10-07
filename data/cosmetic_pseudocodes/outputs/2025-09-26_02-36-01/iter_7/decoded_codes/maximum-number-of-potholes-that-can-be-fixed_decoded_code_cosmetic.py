class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        pts = road.split(".")
        fixCount = 0
        pts.sort(key=len)

        idx = 0
        totalSegments = len(pts)
        while idx < totalSegments:
            currentSegment = pts[idx]
            segmentLength = len(currentSegment)
            if segmentLength <= 0:
                idx += 1
                continue

            reqCost = (segmentLength + 1) * 1

            if reqCost <= budget:
                fixCount += segmentLength
                budget -= reqCost
            else:
                j = segmentLength
                while True:
                    if j <= 0 or budget <= 0:
                        break
                    reqCost = j + 1
                    if budget >= reqCost:
                        fixCount += j
                        budget -= reqCost
                        break
                    j -= 1
            idx += 1

        return fixCount