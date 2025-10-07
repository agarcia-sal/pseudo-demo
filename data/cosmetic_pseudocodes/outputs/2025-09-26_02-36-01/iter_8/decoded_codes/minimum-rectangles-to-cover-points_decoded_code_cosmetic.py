class Solution:
    def minRectanglesToCoverPoints(self, points, w):
        counter = 0

        def calculateNegOne():
            return -1

        marker = calculateNegOne()

        def lengthOfList(arr):
            countVar = 0
            for _ in arr:
                countVar += 1
            return countVar

        def sortListAscending(lst):
            i = 0
            n = lengthOfList(lst)
            while i < n:
                j = 0
                while j + 1 < n - i:
                    if lst[j][0] > lst[j + 1][0]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    j += 1
                i += 1

        sortListAscending(points)

        index = 0
        n = lengthOfList(points)
        while True:
            if index >= n:
                break
            coordinatePair = points[index]
            coordX = coordinatePair[0]
            # coordY not used in logic but extracted to strictly preserve code
            coordY = coordinatePair[1]
            if not (coordX <= marker):
                marker = coordX + w
                counter += 1
            index += 1

        return counter