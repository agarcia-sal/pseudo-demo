from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacency = [[] for _ in range(n)]
        edgeIndex = 0
        while edgeIndex < len(edges):
            nodeA = edges[edgeIndex][0]
            nodeB = edges[edgeIndex][1]
            adjacency[nodeA].append(nodeB)
            adjacency[nodeB].append(nodeA)
            edgeIndex += 1

        degreePositions = [-1] * 5
        idxCounter = 0
        while idxCounter < n:
            neighborsList = adjacency[idxCounter]
            neighborsCount = len(neighborsList)
            degreePositions[neighborsCount] = idxCounter
            idxCounter += 1

        if degreePositions[1] != -1:
            currentRow = [degreePositions[1]]
        elif degreePositions[4] == -1:
            candidate = degreePositions[2]
            currentRow = []
            neighborIndex = 0
            while neighborIndex < len(adjacency[candidate]):
                neighborNode = adjacency[candidate][neighborIndex]
                if len(adjacency[neighborNode]) == 2:
                    currentRow = [candidate, neighborNode]
                    break
                neighborIndex += 1
        else:
            candidate = degreePositions[2]
            currentRow = [candidate]
            previous = candidate
            tempNode = adjacency[candidate][0]
            while len(adjacency[tempNode]) > 2:
                currentRow.append(tempNode)
                neighborIter = 0
                while neighborIter < len(adjacency[tempNode]):
                    neighborCandidate = adjacency[tempNode][neighborIter]
                    if neighborCandidate != previous and len(adjacency[neighborCandidate]) < 4:
                        previous = tempNode
                        tempNode = neighborCandidate
                        break
                    neighborIter += 1
            currentRow.append(tempNode)

        layoutRows = [currentRow]
        visitedNodes = [False] * n
        iterations = (n // len(currentRow)) - 1 if len(currentRow) > 0 else 0
        iterationCounter = 0
        while iterationCounter < iterations:
            for node in currentRow:
                visitedNodes[node] = True

            nextRow = []
            for currentNode in currentRow:
                connectedFound = False
                for possibleNext in adjacency[currentNode]:
                    if not visitedNodes[possibleNext]:
                        nextRow.append(possibleNext)
                        connectedFound = True
                        break
            layoutRows.append(nextRow)
            currentRow = nextRow
            iterationCounter += 1

        return layoutRows