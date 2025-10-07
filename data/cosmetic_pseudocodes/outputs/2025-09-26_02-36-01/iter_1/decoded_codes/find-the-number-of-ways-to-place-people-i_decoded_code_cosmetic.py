class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        length = len(points)
        for firstIndex in range(length):
            x_first, y_first = points[firstIndex]
            for secondIndex in range(length):
                if firstIndex == secondIndex:
                    continue
                x_second, y_second = points[secondIndex]
                if x_first <= x_second and y_first >= y_second:
                    isValidPair = True
                    for midIndex in range(length):
                        if midIndex not in (firstIndex, secondIndex):
                            x_mid, y_mid = points[midIndex]
                            if x_first <= x_mid <= x_second and y_first >= y_mid >= y_second:
                                isValidPair = False
                                break
                    if isValidPair:
                        totalPairs += 1
        return totalPairs