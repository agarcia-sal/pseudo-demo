from collections import defaultdict

class Solution:
    def findAnswer(self, n, edges):
        def extractMin(pqList):
            minIndex = 0
            idx = 1
            while idx < len(pqList):
                if pqList[idx][0] < pqList[minIndex][0]:
                    minIndex = idx
                idx += 1
            minElement = pqList[minIndex]
            pqList[minIndex] = pqList[-1]
            pqList.pop()
            return minElement

        def addHeapElement(pqList, element):
            pqList.append(element)
            i = len(pqList) - 1
            while i > 0:
                parentIdx = (i - 1) // 2
                if pqList[parentIdx][0] > pqList[i][0]:
                    pqList[parentIdx], pqList[i] = pqList[i], pqList[parentIdx]
                    i = parentIdx
                else:
                    break

        adjacencyMap = defaultdict(list)
        for edgeElement in edges:
            firstNode, secondNode, edgeWeight = edgeElement
            adjacencyMap[firstNode].append((secondNode, edgeWeight))
            adjacencyMap[secondNode].append((firstNode, edgeWeight))

        maxDistance = (999999999 + 1) * 10
        minimumDistances = [maxDistance] * n
        minimumDistances[0] = 0

        priorityQueue = []
        addHeapElement(priorityQueue, (0, 0))

        def processPriorityQueue(pq):
            if len(pq) == 0:
                return
            currentPair = extractMin(pq)
            currentDistance, currentNode = currentPair

            if currentDistance > minimumDistances[currentNode]:
                processPriorityQueue(pq)
                return

            neighborIndex = 0
            neighbors = adjacencyMap[currentNode]
            while neighborIndex < len(neighbors):
                nextNode, travelCost = neighbors[neighborIndex]
                newDistance = currentDistance + travelCost
                if newDistance < minimumDistances[nextNode]:
                    minimumDistances[nextNode] = newDistance
                    addHeapElement(pq, (newDistance, nextNode))
                neighborIndex += 1
            processPriorityQueue(pq)

        processPriorityQueue(priorityQueue)

        importantEdges = set()
        dfsStack = [(n - 1, minimumDistances[n - 1])]
        discovered = [0] * n

        def dfsVisit(stack):
            if len(stack) == 0:
                return
            topElement = stack.pop()
            nodeId, distAtNode = topElement

            if discovered[nodeId] == 1:
                dfsVisit(stack)
                return

            discovered[nodeId] = 1

            idx = 0
            neighbors = adjacencyMap[nodeId]
            while idx < len(neighbors):
                neighbor, weightVal = neighbors[idx]
                if distAtNode == minimumDistances[neighbor] + weightVal:
                    edgePair = (nodeId, neighbor) if nodeId < neighbor else (neighbor, nodeId)
                    importantEdges.add(edgePair)
                    stack.append((neighbor, minimumDistances[neighbor]))
                idx += 1
            dfsVisit(stack)

        dfsVisit(dfsStack)

        resultList = []
        idxLoop = 0
        while idxLoop < len(edges):
            currEdge = edges[idxLoop]
            startNode, endNode = currEdge[0], currEdge[1]
            orderedEdge = (startNode, endNode) if startNode < endNode else (endNode, startNode)
            resultList.append(orderedEdge in importantEdges)
            idxLoop += 1

        finalAnswer = resultList
        return finalAnswer