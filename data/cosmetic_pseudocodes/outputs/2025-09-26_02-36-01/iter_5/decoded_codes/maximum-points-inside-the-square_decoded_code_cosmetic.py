class Solution:
    def maxPointsInsideSquare(self, params):
        def withinBounds(val, limit):
            return -limit <= val <= limit

        def enumerateIndices(current, endIndex, actionFunc):
            if current > endIndex:
                return
            actionFunc(current)
            enumerateIndices(current + 1, endIndex, actionFunc)

        totalCount = 0
        upperBound = len(params)

        def processIndex(index):
            nonlocal totalCount
            coordX, coordY = params[index]
            maxSide = abs(coordX) if abs(coordX) > abs(coordY) else abs(coordY)
            seenTags = {}
            isValidSquare = True

            def checkIndex(innerIdx):
                nonlocal isValidSquare
                candidateX, candidateY = params[innerIdx]
                if withinBounds(candidateX, maxSide) and withinBounds(candidateY, maxSide):
                    currentTag = params[innerIdx]
                    if currentTag in seenTags:
                        isValidSquare = False
                        return
                    else:
                        seenTags[currentTag] = 1

            enumerateIndices(0, upperBound - 1, checkIndex)
            if isValidSquare:
                totalCount = max(totalCount, len(seenTags))

        enumerateIndices(0, upperBound - 1, processIndex)

        return totalCount