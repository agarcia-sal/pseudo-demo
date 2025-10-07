class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        size = len(points)
        for outerIndex in range(size):
            for innerIndex in range(size):
                if outerIndex != innerIndex:
                    x_outer, y_outer = points[outerIndex]
                    x_inner, y_inner = points[innerIndex]
                    if x_outer <= x_inner and y_outer >= y_inner:
                        isValid = True
                        for checkIndex in range(size):
                            if checkIndex != outerIndex and checkIndex != innerIndex:
                                x_check, y_check = points[checkIndex]
                                if x_outer <= x_check <= x_inner and y_outer >= y_check >= y_inner:
                                    isValid = False
                                    break
                        if isValid:
                            totalPairs += 1
        return totalPairs