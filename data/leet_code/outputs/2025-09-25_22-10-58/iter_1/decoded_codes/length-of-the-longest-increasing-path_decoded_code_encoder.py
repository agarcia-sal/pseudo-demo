from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates, k):
        xk = coordinates[k][0]
        yk = coordinates[k][1]
        leftCoordinates = [(x, y) for x, y in coordinates if x < xk and y < yk]
        rightCoordinates = [(x, y) for x, y in coordinates if x > xk and y > yk]
        return 1 + self._lengthOfLIS(leftCoordinates) + self._lengthOfLIS(rightCoordinates)

    def _lengthOfLIS(self, coordinates):
        # Sort by x ascending and by y descending when x is equal
        coordinates.sort(key=lambda c: (c[0], -c[1]))
        tail = []
        for _, y in coordinates:
            if not tail or y > tail[-1]:
                tail.append(y)
            else:
                pos = bisect_left(tail, y)
                tail[pos] = y
        return len(tail)