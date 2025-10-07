from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graphContainer = [[] for _ in range(n)]

        def addEdgePair(a: int, b: int) -> None:
            graphContainer[a].append(b)
            graphContainer[b].append(a)

        for sourceNode, targetNode in edges:
            addEdgePair(sourceNode, targetNode)

        degreeList = [-1] * 5
        for idx in range(n):
            connectedNodes = graphContainer[idx]
            degreeList[len(connectedNodes)] = idx

        if degreeList[1] != -1:
            startingRow = [degreeList[1]]
        elif degreeList[4] == -1:
            baseNode = degreeList[2]
            candidateNode = None
            for neighborNode in graphContainer[baseNode]:
                if len(graphContainer[neighborNode]) == 2:
                    candidateNode = neighborNode
                    break
            startingRow = [baseNode, candidateNode]
        else:
            currentNode = degreeList[2]
            startingRow = [currentNode]
            previousNode = currentNode
            currentNode = graphContainer[currentNode][0]
            while len(graphContainer[currentNode]) > 2:
                startingRow.append(currentNode)
                for neighborNode in graphContainer[currentNode]:
                    if neighborNode != previousNode and len(graphContainer[neighborNode]) < 4:
                        previousNode = currentNode
                        currentNode = neighborNode
                        break
            startingRow.append(currentNode)

        answerGrid = [startingRow]
        visitedFlags = [False] * n
        repeatCount = (n // len(startingRow)) - 1
        repetition = 0

        while repetition < repeatCount:
            for nodeVal in startingRow:
                visitedFlags[nodeVal] = True

            nextRow = []
            for nodeVal in startingRow:
                for adjNode in graphContainer[nodeVal]:
                    if not visitedFlags[adjNode]:
                        nextRow.append(adjNode)
                        break

            answerGrid.append(nextRow)
            startingRow = nextRow
            repetition += 1

        return answerGrid