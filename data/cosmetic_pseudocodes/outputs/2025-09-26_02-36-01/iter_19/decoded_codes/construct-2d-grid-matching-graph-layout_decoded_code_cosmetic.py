from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacencyMatrix = [[] for _ in range(n)]
        for sourceNode, targetNode in edges:
            adjacencyMatrix[sourceNode].append(targetNode)
            adjacencyMatrix[targetNode].append(sourceNode)

        degrees = [-1] * 5  # degrees[i] stores a node with degree i, or -1 if none
        for nodeIndex, neighbors in enumerate(adjacencyMatrix):
            deg = len(neighbors)
            if 0 <= deg < 5:
                degrees[deg] = nodeIndex

        if degrees[1] != -1:
            currentRow = [degrees[1]]
        elif degrees[4] == -1:
            candidateNode = degrees[2]
            currentRow = []
            for candidateNeighbor in adjacencyMatrix[candidateNode]:
                if len(adjacencyMatrix[candidateNeighbor]) == 2:
                    currentRow = [candidateNode, candidateNeighbor]
                    break
        else:
            candidateNode = degrees[2]
            currentRow = [candidateNode]
            previousNode = candidateNode
            candidateNode = adjacencyMatrix[candidateNode][0]

            while len(adjacencyMatrix[candidateNode]) > 2:
                currentRow.append(candidateNode)
                for neighborNode in adjacencyMatrix[candidateNode]:
                    if neighborNode != previousNode and len(adjacencyMatrix[neighborNode]) < 4:
                        previousNode = candidateNode
                        candidateNode = neighborNode
                        break
            currentRow.append(candidateNode)

        answer = [currentRow]
        visitedFlags = [False] * n

        row_length = len(currentRow)
        iterations = (n // row_length) - 1

        for _ in range(iterations):
            for nodeIndex in currentRow:
                visitedFlags[nodeIndex] = True

            nextRow = []
            for nodeIndex in currentRow:
                for neighborNode in adjacencyMatrix[nodeIndex]:
                    if not visitedFlags[neighborNode]:
                        nextRow.append(neighborNode)
                        break

            answer.append(nextRow)
            currentRow = nextRow

        return answer