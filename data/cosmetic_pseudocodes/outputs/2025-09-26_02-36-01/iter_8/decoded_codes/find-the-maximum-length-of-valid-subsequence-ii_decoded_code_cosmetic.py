class Solution:
    def maximumLength(self, nums, k):
        totalCount = len(nums)
        if not (totalCount > 1):
            return 1

        def createMapList(mCount):
            container = []
            while mCount > 0:
                mCount -= 1
                container.append({})
            return container

        trackers = createMapList(totalCount)
        currentMax = 1
        indexOuter = 0
        while indexOuter != totalCount:
            indexInner = 0
            limitInner = indexOuter - 1
            while indexInner < limitInner:
                sumVal = nums[indexOuter] + nums[indexInner]
                modResult = sumVal - (k * (sumVal // k))

                mapInner = trackers[indexInner]
                mapOuter = trackers[indexOuter]

                if modResult in mapInner:
                    mapOuter[modResult] = mapInner[modResult] + 1
                else:
                    mapOuter[modResult] = 2

                if mapOuter[modResult] > currentMax:
                    currentMax = mapOuter[modResult]

                indexInner += 1
            indexOuter += 1

        return currentMax