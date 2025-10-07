class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        segments = []
        partsIndex = 0  # zero-based index for Python strings
        currentSegment = ""

        # Manually split 'road' by '.' into 'segments'
        while partsIndex <= len(road):
            ch = road[partsIndex] if partsIndex < len(road) else ""
            if ch == "." or ch == "":
                segments.append(currentSegment)
                currentSegment = ""
            else:
                currentSegment += ch
            partsIndex += 1

        # Bubble sort segments by ascending length
        changed = True
        while changed:
            changed = False
            for i in range(len(segments) - 1):
                if len(segments[i]) > len(segments[i + 1]):
                    segments[i], segments[i + 1] = segments[i + 1], segments[i]
                    changed = True

        countFixed = 0
        idx = 0

        while idx < len(segments):
            lengthSeg = len(segments[idx])

            if lengthSeg != 0:
                perCost = lengthSeg + 1
                if budget >= perCost:
                    countFixed += lengthSeg
                    budget -= perCost
                else:
                    subLength = lengthSeg
                    while subLength > 0 and budget > 0:
                        perCost = subLength + 1
                        if budget >= perCost:
                            countFixed += subLength
                            budget -= perCost
                            break
                        subLength -= 1
            idx += 1

        return countFixed