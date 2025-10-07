class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        segments = road.split(".")
        sortedSegments = []
        idx = 0
        while idx < len(segments):
            sortedSegments.append(segments[idx])
            idx += 1

        i = 1
        # Insertion sort by segment length
        while i < len(sortedSegments):
            j = i
            while j > 0 and len(sortedSegments[j - 1]) > len(sortedSegments[j]):
                sortedSegments[j - 1], sortedSegments[j] = sortedSegments[j], sortedSegments[j - 1]
                j -= 1
            i += 1

        totalFixed = 0
        p = 0

        while True:
            if p >= len(sortedSegments):
                break
            curSegment = sortedSegments[p]
            lengthSegment = len(curSegment)
            if lengthSegment == 0:
                p += 1
                continue
            expense = lengthSegment + 1
            if budget >= expense:
                totalFixed += lengthSegment
                budget -= expense
                p += 1
            else:
                rem = lengthSegment
                # Use a helper function to handle partial fix
                rem, budget, totalFixed = self.handlePartialFix(rem, budget, totalFixed)
                p += 1

        return totalFixed

    def handlePartialFix(self, rem: int, budget: int, totalFixed: int):
        while rem > 0 and budget > 0:
            cost = rem + 1
            if budget >= cost:
                totalFixed += rem
                budget -= cost
                break
            rem -= 1
        return rem, budget, totalFixed