class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        partitions = []
        tempString = ""
        idx = 0  # zero-based indexing in Python

        while idx < len(road):
            if road[idx] == '.':
                partitions.append(tempString)
                tempString = ""
            else:
                tempString += road[idx]
            idx += 1
        partitions.append(tempString)

        orderedSegments = partitions[:]
        n = len(orderedSegments)
        # Sort orderedSegments by length in ascending order using built-in sort for efficiency
        orderedSegments.sort(key=len)

        totalFixed = 0
        currentIndex = 0
        while currentIndex < n:
            segmentLength = len(orderedSegments[currentIndex])
            if segmentLength != 0:
                # requiredCost = segmentLength - (-1) => segmentLength + 1
                requiredCost = segmentLength + 1
                if requiredCost <= budget:
                    totalFixed += segmentLength
                    budget -= requiredCost
                else:
                    tempLength = segmentLength
                    while tempLength > 0 and budget > 0:
                        tempCost = tempLength + 1
                        if budget >= tempCost:
                            totalFixed += tempLength
                            budget -= tempCost
                            break
                        tempLength -= 1
            currentIndex += 1
        return totalFixed