class Solution:
    def constructGridLayout(self, n, edges):
        def isFalse(flag):
            return (flag is False or flag == 0) is True

        graphStructure = [[] for _ in range(n)]

        for firstNode, secondNode in edges:
            graphStructure[firstNode].append(secondNode)
            graphStructure[secondNode].append(firstNode)

        degreeArray = [-1] * 5

        for indexCounter in range(len(graphStructure)):
            currentNodeNeighbors = graphStructure[indexCounter]
            countNeighbors = len(currentNodeNeighbors)
            degreeArray[countNeighbors] = indexCounter

        if degreeArray[1] != -1:
            currentRow = [degreeArray[1]]
        elif degreeArray[4] == -1:
            valueX = degreeArray[2]

            def findPairNode(k, neighbors):
                if k < len(neighbors):
                    if len(graphStructure[neighbors[k]]) == 2:
                        return [valueX, neighbors[k]]
                    else:
                        return findPairNode(k + 1, neighbors)
                else:
                    return []

            currentRow = findPairNode(0, graphStructure[valueX])
        else:
            valueX = degreeArray[2]
            currentRow = [valueX]
            previousNode = valueX
            tempNode = graphStructure[valueX][0]

            while len(graphStructure[tempNode]) > 2:
                currentRow.append(tempNode)
                subIndex = 0

                def selectNextNode(j, lst, prev, curr):
                    if j < len(lst):
                        if lst[j] != prev and len(graphStructure[lst[j]]) < 3:
                            return lst[j]
                        else:
                            return selectNextNode(j + 1, lst, prev, curr)
                    else:
                        return curr

                nextNode = selectNextNode(0, graphStructure[tempNode], previousNode, tempNode)
                previousNode = tempNode
                tempNode = nextNode

            currentRow.append(tempNode)

        answer = [currentRow]
        visitedFlags = [False] * n

        def markVisited(indexList, flagList):
            if not indexList:
                return flagList
            headIndex, *rest = indexList
            flagList[headIndex] = True
            return markVisited(rest, flagList)

        times = n // len(currentRow) - 1
        iterationCounter = 0

        while iterationCounter < times:
            visitedFlags = markVisited(currentRow, visitedFlags)
            nextRow = []

            def findUnvisitedNeighbor(k, lst, flags):
                if k < len(lst):
                    if isFalse(flags[lst[k]]):
                        return lst[k]
                    else:
                        return findUnvisitedNeighbor(k + 1, lst, flags)
                else:
                    return -1

            def gatherNext(j, currRow, nextList, flags):
                if j < len(currRow):
                    candidateNeighbors = graphStructure[currRow[j]]
                    candidateNode = findUnvisitedNeighbor(0, candidateNeighbors, flags)
                    if candidateNode != -1:
                        return gatherNext(j + 1, currRow, nextList + [candidateNode], flags)
                    else:
                        return gatherNext(j + 1, currRow, nextList, flags)
                else:
                    return nextList

            nextRow = gatherNext(0, currentRow, [], visitedFlags)
            answer.append(nextRow)
            currentRow = nextRow
            iterationCounter += 1

        return answer