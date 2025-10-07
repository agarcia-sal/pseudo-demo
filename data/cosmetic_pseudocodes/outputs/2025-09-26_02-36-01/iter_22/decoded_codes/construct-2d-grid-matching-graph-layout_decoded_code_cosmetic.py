class Solution:
    def constructGridLayout(self, n, edges):
        adjacency = [[] for _ in range(n)]
        for edge in edges:
            nodeA, nodeB = edge
            adjacency[nodeA].append(nodeB)
            adjacency[nodeB].append(nodeA)

        degreePositions = [-1] * 5
        for posIndex, neighbors in enumerate(adjacency):
            degreePositions[len(neighbors)] = posIndex

        if degreePositions[1] != -1:
            currentRow = [degreePositions[1]]
        elif degreePositions[4] == -1:
            centralNode = degreePositions[2]
            candidateFound = False
            for neighborNode in adjacency[centralNode]:
                if len(adjacency[neighborNode]) == 2:
                    currentRow = [centralNode, neighborNode]
                    candidateFound = True
                    break
            if not candidateFound:
                currentRow = []
        else:
            centralNode = degreePositions[2]
            currentRow = [centralNode]
            previousNode = centralNode
            adjacentNodeCandidates = adjacency[centralNode]
            nextNode = adjacentNodeCandidates[0]

            while len(adjacency[nextNode]) > 2:
                currentRow.append(nextNode)
                foundNext = False
                for neighborCandidate in adjacency[nextNode]:
                    if neighborCandidate != previousNode and len(adjacency[neighborCandidate]) < 4:
                        previousNode = nextNode
                        nextNode = neighborCandidate
                        foundNext = True
                        break
                if not foundNext:
                    break
            currentRow.append(nextNode)

        layoutRows = [currentRow]
        visitedNodes = [False] * n
        if len(currentRow) == 0:
            iterations = 0
        else:
            iterations = (n // len(currentRow)) - 1
        iterationCounter = 0

        while iterationCounter < iterations:
            for node in currentRow:
                visitedNodes[node] = True

            nextRow = []
            for node in currentRow:
                for adjacentNode in adjacency[node]:
                    if not visitedNodes[adjacentNode]:
                        nextRow.append(adjacentNode)
                        break

            layoutRows.append(nextRow)
            currentRow = nextRow
            iterationCounter += 1

        return layoutRows