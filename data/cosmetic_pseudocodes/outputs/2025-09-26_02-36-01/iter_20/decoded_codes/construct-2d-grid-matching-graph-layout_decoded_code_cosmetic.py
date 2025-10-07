class Solution:
    def constructGridLayout(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        def createEmptyBuckets(m: int) -> list[list[int]]:
            bucketList = []
            counter = 0
            while counter < m:
                bucketList.append([])
                counter += 1
            return bucketList

        def listAllFalse(size: int) -> list[bool]:
            collection = []
            idxVar = 0
            while idxVar < size:
                collection.append(False)
                idxVar += 1
            return collection

        def findIndexForDegree(array: list[list[int]], targetValue: int) -> int:
            finder = 0
            while finder < len(array):
                if len(array[finder]) == targetValue:
                    return finder
                finder += 1
            return -1

        graphStructure = createEmptyBuckets(n)
        edgeIterator = 0
        while edgeIterator < len(edges):
            nodeM = edges[edgeIterator][0]
            nodeN = edges[edgeIterator][1]
            graphStructure[nodeM].append(nodeN)
            graphStructure[nodeN].append(nodeM)
            edgeIterator += 1

        degreeIndices = [-1, -1, -1, -1, -1]
        positionTracker = 0
        while positionTracker < n:
            currentEdges = graphStructure[positionTracker]
            idxPosition = len(currentEdges)
            degreeIndices[idxPosition] = positionTracker
            positionTracker += 1

        if degreeIndices[1] != -1:
            initialRow = [degreeIndices[1]]
        elif degreeIndices[4] == -1:
            firstCandidate = degreeIndices[2]
            foundFlag = False
            jumpIndex = 0
            while not foundFlag and jumpIndex < len(graphStructure[firstCandidate]):
                adjacentNode = graphStructure[firstCandidate][jumpIndex]
                if len(graphStructure[adjacentNode]) == 2:
                    initialRow = [firstCandidate, adjacentNode]
                    foundFlag = True
                jumpIndex += 1
        else:
            firstCandidate = degreeIndices[2]
            initialRow = [firstCandidate]
            previousNode = firstCandidate
            currentNode = graphStructure[firstCandidate][0]
            while True:
                if len(graphStructure[currentNode]) > 2:
                    initialRow.append(currentNode)
                    innerIter = 0
                    foundNext = False
                    while innerIter < len(graphStructure[currentNode]):
                        neighbourNode = graphStructure[currentNode][innerIter]
                        if neighbourNode != previousNode and len(graphStructure[neighbourNode]) < 4:
                            previousNode = currentNode
                            currentNode = neighbourNode
                            foundNext = True
                            break
                        innerIter += 1
                    if not foundNext:
                        break
                else:
                    break
            initialRow.append(currentNode)

        resultList = [initialRow]
        visitedNodes = listAllFalse(n)
        row_length = len(initialRow)
        maxRepeats = (n // row_length) - 1
        repeatCount = 0

        while repeatCount < maxRepeats:
            markIndex = 0
            while markIndex < row_length:
                visitedNodes[initialRow[markIndex]] = True
                markIndex += 1

            nextRowCandidates = []
            outerIndex = 0
            while outerIndex < row_length:
                curIndex = initialRow[outerIndex]
                innerIndex = 0
                foundInNext = False
                while not foundInNext and innerIndex < len(graphStructure[curIndex]):
                    candidateNode = graphStructure[curIndex][innerIndex]
                    if not visitedNodes[candidateNode]:
                        nextRowCandidates.append(candidateNode)
                        foundInNext = True
                    innerIndex += 1
                outerIndex += 1

            resultList.append(nextRowCandidates)
            initialRow = nextRowCandidates
            repeatCount += 1

        return resultList