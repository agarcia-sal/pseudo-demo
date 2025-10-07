class Solution:
    def maxSelectedElements(self, nums):
        resultVar = 0
        trackingMap = dict()
        orderedNums = sorted(nums)
        indexIter = 0
        while indexIter < len(orderedNums):
            currItem = orderedNums[indexIter]
            if currItem + 1 in trackingMap:
                trackingMap[currItem + 1] = trackingMap[currItem + 1]
            else:
                trackingMap[currItem + 1] = 0
            trackingMap[currItem + 1] += 1

            if currItem - 1 in trackingMap:
                trackingMap[currItem] = trackingMap[currItem - 1] + 1
            else:
                trackingMap[currItem] = 1

            tempMax = resultVar
            if tempMax < trackingMap[currItem]:
                tempMax = trackingMap[currItem]
            if tempMax < trackingMap[currItem + 1]:
                tempMax = trackingMap[currItem + 1]
            resultVar = tempMax
            indexIter += 1
        return resultVar