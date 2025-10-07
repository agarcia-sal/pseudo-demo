class Solution:
    def constructGridLayout(self, n, edges):
        def createEmptyLists(count):
            return [[] for _ in range(count)]

        def hasValue(lst, val):
            flag = False
            i = 0
            while i < len(lst) and not flag:
                if lst[i] == val:
                    flag = True
                i += 1
            return flag

        def computeDegreePositions(graph):
            degreeList = [-1, -1, -1, -1, -1]
            idx2 = 0
            while idx2 < len(graph):
                l = len(graph[idx2])
                degreeList[l] = idx2
                idx2 += 1
            return degreeList

        def buildRowWhenOnePresent(degreePositions):
            return [degreePositions[1]]

        def buildRowWhenFourMissing(degreePositions, graph):
            candidateX = degreePositions[2]
            candidateRow = []
            idxY = 0
            rowFound = False
            while idxY < len(graph[candidateX]) and not rowFound:
                candidateY = graph[candidateX][idxY]
                if len(graph[candidateY]) == 2:
                    candidateRow = [candidateX, candidateY]
                    rowFound = True
                idxY += 1
            return candidateRow

        def buildRowComplex(degreePositions, graph):
            principalX = degreePositions[2]
            lineage = [principalX]
            precursor = principalX
            successor = graph[principalX][0]
            while len(graph[successor]) > 2:
                lineage.append(successor)
                idxY = 0
                updated = False
                while idxY < len(graph[successor]) and not updated:
                    candidateY = graph[successor][idxY]
                    if candidateY != precursor and len(graph[candidateY]) < 4:
                        precursor = successor
                        successor = candidateY
                        updated = True
                    idxY += 1
            lineage.append(successor)
            return lineage

        def markVisited(positions, visited):
            i = 0
            while i < len(positions):
                visited[positions[i]] = True
                i += 1

        def findNextRow(currentRow, graph, visited):
            newRow = []
            ri = 0
            while ri < len(currentRow):
                cx = currentRow[ri]
                yi = 0
                found = False
                while yi < len(graph[cx]) and not found:
                    if not visited[graph[cx][yi]]:
                        newRow.append(graph[cx][yi])
                        found = True
                    yi += 1
                ri += 1
            return newRow

        graphRep = createEmptyLists(n)

        eIndex = 0
        while eIndex < len(edges):
            uPrime, vPrime = edges[eIndex]
            graphRep[uPrime].append(vPrime)
            graphRep[vPrime].append(uPrime)
            eIndex += 1

        degrees = computeDegreePositions(graphRep)

        assembledRow = []
        if degrees[1] != -1:
            assembledRow = buildRowWhenOnePresent(degrees)
        elif degrees[4] == -1:
            assembledRow = buildRowWhenFourMissing(degrees, graphRep)
        else:
            assembledRow = buildRowComplex(degrees, graphRep)

        arrangement = [assembledRow]
        visitedList = [False] * n

        loopsCount = (n // len(assembledRow)) - 1 if len(assembledRow) > 0 else 0
        loopIter = 0
        while loopIter < loopsCount:
            markVisited(assembledRow, visitedList)
            assembledRow = findNextRow(assembledRow, graphRep, visitedList)
            arrangement.append(assembledRow)
            loopIter += 1

        return arrangement