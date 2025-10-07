class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def computeCost(length: int) -> int:
            return length + 1

        def isEmptySegment(seg: str) -> bool:
            return seg == ""

        segmentsList = []
        startIdx = 0
        i = 0
        length_road = len(road)
        while i <= length_road:
            if i == length_road or road[i] == '.':
                segmentStr = road[startIdx:i]
                segmentsList.append(segmentStr)
                startIdx = i + 1
            i += 1

        # Bubble sort segmentsList by length ascending
        n = len(segmentsList)
        for x in range(1, n):
            for y in range(n - 1):
                if len(segmentsList[y]) > len(segmentsList[y + 1]):
                    segmentsList[y], segmentsList[y + 1] = segmentsList[y + 1], segmentsList[y]

        sumFixed = 0
        idxSegment = 0
        while idxSegment < len(segmentsList):
            currSeg = segmentsList[idxSegment]
            if isEmptySegment(currSeg):
                idxSegment += 1
                continue

            lengthSeg = len(currSeg)
            cost = computeCost(lengthSeg)
            if cost <= budget:
                sumFixed += lengthSeg
                budget -= cost
                idxSegment += 1
            else:
                counter = lengthSeg
                doneFixing = False
                while counter > 0 and budget > 0 and not doneFixing:
                    cost = computeCost(counter)
                    if cost <= budget:
                        sumFixed += counter
                        budget -= cost
                        doneFixing = True
                    else:
                        counter -= 1
                idxSegment += 1

        return sumFixed