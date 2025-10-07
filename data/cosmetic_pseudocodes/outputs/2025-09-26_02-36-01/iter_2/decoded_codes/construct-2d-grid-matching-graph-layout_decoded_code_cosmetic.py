class Solution:
    def constructGridLayout(self, n, edges):
        adjacencyList = [[] for _ in range(n)]
        for edgePair in edges:
            nodeA, nodeB = edgePair
            adjacencyList[nodeA].append(nodeB)
            adjacencyList[nodeB].append(nodeA)

        degreePositions = [-1] * 5
        for idx, neighbors in enumerate(adjacencyList):
            degreePositions[len(neighbors)] = idx

        if degreePositions[1] != -1:
            currentRow = [degreePositions[1]]
        elif degreePositions[4] == -1:
            startingNode = degreePositions[2]
            neighborCandidate = None
            for candidate in adjacencyList[startingNode]:
                if len(adjacencyList[candidate]) == 2:
                    neighborCandidate = candidate
                    break
            currentRow = [startingNode, neighborCandidate]
        else:
            previousNode = degreePositions[2]
            currentRow = [previousNode]
            nextNode = adjacencyList[previousNode][0]
            while len(adjacencyList[nextNode]) > 2:
                currentRow.append(nextNode)
                for neighbor in adjacencyList[nextNode]:
                    if neighbor != previousNode and len(adjacencyList[neighbor]) < 4:
                        previousNode = nextNode
                        nextNode = neighbor
                        break
            currentRow.append(nextNode)

        answerGrid = [currentRow]
        visitedNodes = [False] * n
        iterations = (n // len(currentRow)) - 1
        i = 0
        while i < iterations:
            for node in currentRow:
                visitedNodes[node] = True

            nextRow = []
            for node in currentRow:
                for neighbor in adjacencyList[node]:
                    if not visitedNodes[neighbor]:
                        nextRow.append(neighbor)
                        break

            answerGrid.append(nextRow)
            currentRow = nextRow
            i += 1

        return answerGrid