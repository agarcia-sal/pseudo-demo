from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graphAdj = [[] for _ in range(n)]

        def addEdges(index: int):
            if index == len(edges):
                return
            nodeA, nodeB = edges[index]
            graphAdj[nodeA].append(nodeB)
            graphAdj[nodeB].append(nodeA)
            addEdges(index + 1)

        addEdges(0)

        degreeMap = [-1] * 5
        pos = 0
        while pos < len(graphAdj):
            neighbors = graphAdj[pos]
            idx = len(neighbors)
            degreeMap[idx] = pos
            pos += 1

        resultRow = []
        if degreeMap[1] != -1:
            resultRow = [degreeMap[1]]
        else:
            if degreeMap[4] == -1:
                centralNode = degreeMap[2]
                foundRow = False

                def findRow(nodes: List[int], pos: int):
                    nonlocal foundRow, resultRow
                    if pos == len(nodes) or foundRow:
                        return
                    candidate = nodes[pos]
                    if len(graphAdj[candidate]) == 2:
                        resultRow = [centralNode, candidate]
                        foundRow = True
                        return
                    findRow(nodes, pos + 1)

                findRow(graphAdj[centralNode], 0)
            else:
                currentNode = degreeMap[2]
                resultRow = [currentNode]
                previousNode = currentNode
                adjNodes = graphAdj[currentNode]
                currentNode = adjNodes[0]

                def traverseChain(prev: int, curr: int):
                    nonlocal resultRow
                    while len(graphAdj[curr]) > 2:
                        resultRow.append(curr)
                        adjVals = graphAdj[curr]
                        i = 0
                        while i < len(adjVals):
                            neighbor = adjVals[i]
                            if neighbor != prev and len(graphAdj[neighbor]) < 4:
                                prev = curr
                                curr = neighbor
                                break
                            i += 1
                        else:
                            # No unvisited suitable neighbor found, break to avoid infinite loop
                            break
                    resultRow.append(curr)

                traverseChain(previousNode, currentNode)

        outputGrid = [resultRow]
        visitedNodes = [False] * n
        iterCount = (n // len(resultRow)) - 1

        def markVisited(nodes: List[int]):
            for idx in range(len(nodes)):
                visitedNodes[nodes[idx]] = True

        def buildNextRow(currentRow: List[int]) -> List[int]:
            nextRow = []
            for nodeVal in currentRow:
                neighbors = graphAdj[nodeVal]
                j = 0
                while j < len(neighbors):
                    neighborNode = neighbors[j]
                    if not visitedNodes[neighborNode]:
                        nextRow.append(neighborNode)
                        break
                    j += 1
            return nextRow

        loopCounter = 0
        while loopCounter < iterCount:
            markVisited(resultRow)
            resultRow = buildNextRow(resultRow)
            outputGrid.append(resultRow)
            loopCounter += 1

        return outputGrid