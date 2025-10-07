from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        emptyGraph = [[] for _ in range(n)]
        idxCurrent = 0
        while idxCurrent < len(edges):
            nodeA = edges[idxCurrent][0]
            nodeB = edges[idxCurrent][1]
            emptyGraph[nodeA].append(nodeB)
            emptyGraph[nodeB].append(nodeA)
            idxCurrent += 1

        degreeMapping = [-1] * 5
        iterIndex = 0
        tableau = emptyGraph
        while True:
            if iterIndex >= len(tableau):
                break
            neighborsList = tableau[iterIndex]
            degreeMapping[len(neighborsList)] = iterIndex
            iterIndex += 1

        if degreeMapping[1] != -1:
            activeRow = [degreeMapping[1]]
        else:
            if degreeMapping[4] == -1:
                selectedNode = degreeMapping[2]
                potentialRow = []
                neighborsOfSelected = tableau[selectedNode]
                iterNeighbor = 0
                while iterNeighbor < len(neighborsOfSelected):
                    candidate = neighborsOfSelected[iterNeighbor]
                    if len(tableau[candidate]) == 2:
                        potentialRow = [selectedNode, candidate]
                        break
                    iterNeighbor += 1
                activeRow = potentialRow
            else:
                startNode = degreeMapping[2]
                activeRow = [startNode]
                previousNode = startNode
                candidates = tableau[startNode]
                proceedNode = candidates[0]
                while len(tableau[proceedNode]) > 2:
                    activeRow.append(proceedNode)
                    neighborsList = tableau[proceedNode]
                    neighborsIter = 0
                    while neighborsIter < len(neighborsList):
                        candidateNeighbor = neighborsList[neighborsIter]
                        if candidateNeighbor != previousNode and len(tableau[candidateNeighbor]) < 4:
                            previousNode = proceedNode
                            proceedNode = candidateNeighbor
                            break
                        neighborsIter += 1
                activeRow.append(proceedNode)

        resultGrid = [activeRow]
        visitedFlags = [False] * n

        loopCounter = 1
        totalIterations = (n // len(activeRow)) - 1
        while loopCounter <= totalIterations:
            idxMark = 0
            while idxMark < len(activeRow):
                visitedFlags[activeRow[idxMark]] = True
                idxMark += 1
            nextLevelRow = []
            idxCurrentInner = 0
            while idxCurrentInner < len(activeRow):
                currentElement = activeRow[idxCurrentInner]
                currentNeighbors = tableau[currentElement]
                idxNeighbor = 0
                while idxNeighbor < len(currentNeighbors):
                    neighborElement = currentNeighbors[idxNeighbor]
                    if not visitedFlags[neighborElement]:
                        nextLevelRow.append(neighborElement)
                        break
                    idxNeighbor += 1
                idxCurrentInner += 1
            resultGrid.append(nextLevelRow)
            activeRow = nextLevelRow
            loopCounter += 1

        return resultGrid