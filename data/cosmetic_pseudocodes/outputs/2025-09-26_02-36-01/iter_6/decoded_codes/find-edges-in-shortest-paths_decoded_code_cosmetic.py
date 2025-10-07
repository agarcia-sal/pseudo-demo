class Solution:
    def findAnswer(self, p, q):
        def insertIntoHeap(heapArr, item):
            idx = len(heapArr)
            heapArr.append(item)
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if heapArr[parentIdx][0] > heapArr[idx][0]:
                    heapArr[parentIdx], heapArr[idx] = heapArr[idx], heapArr[parentIdx]
                    idx = parentIdx
                else:
                    break

        def popHeap(heapArr):
            if len(heapArr) == 0:
                return None
            topElement = heapArr[0]
            lastIndex = len(heapArr) - 1
            heapArr[0] = heapArr[lastIndex]
            heapArr.pop()
            current = 0
            while True:
                leftChild = current * 2 + 1
                rightChild = current * 2 + 2
                smallest = current
                if leftChild < len(heapArr) and heapArr[leftChild][0] < heapArr[smallest][0]:
                    smallest = leftChild
                if rightChild < len(heapArr) and heapArr[rightChild][0] < heapArr[smallest][0]:
                    smallest = rightChild
                if smallest == current:
                    break
                heapArr[current], heapArr[smallest] = heapArr[smallest], heapArr[current]
                current = smallest
            return topElement

        def buildGraph(edgesList):
            mapping = dict()
            for i in range(len(edgesList) - 1, -1, -1):
                a, b, c = edgesList[i]
                if a not in mapping:
                    mapping[a] = []
                mapping[a].append((b, c))
                if b not in mapping:
                    mapping[b] = []
                mapping[b].append((a, c))
            return mapping

        def dijkstra(numNodes, graphData):
            distances = [10] * numNodes
            distances[0] = 0
            heap = []
            insertIntoHeap(heap, (0, 0))

            def process():
                if len(heap) == 0:
                    return
                currentEntry = popHeap(heap)
                currDist, nodeIdx = currentEntry
                if currDist > distances[nodeIdx]:
                    process()
                    return
                if nodeIdx in graphData:
                    neighbors = graphData[nodeIdx]
                    for idx in range(len(neighbors) - 1, -1, -1):
                        nextNode, weight = neighbors[idx]
                        possibleDist = currDist + weight
                        if possibleDist < distances[nextNode]:
                            distances[nextNode] = possibleDist
                            insertIntoHeap(heap, (possibleDist, nextNode))
                process()

            process()
            return distances

        def findSPEdges(graphData, distArray, nodeCount):
            spEdges = set()
            stackList = []
            lastNode = nodeCount - 1
            stackList.append((lastNode, distArray[lastNode]))
            visitedArr = [False] * nodeCount

            def exploreStack():
                if len(stackList) == 0:
                    return
                currentPair = stackList.pop()
                currNode, currDist = currentPair
                if visitedArr[currNode]:
                    exploreStack()
                    return
                visitedArr[currNode] = True
                if currNode in graphData:
                    adjacents = graphData[currNode]
                    for j in range(len(adjacents) - 1, -1, -1):
                        neighbor, cost = adjacents[j]
                        if currDist == distArray[neighbor] + cost:
                            lesserVal, greaterVal = currNode, neighbor
                            if neighbor < currNode:
                                lesserVal, greaterVal = neighbor, currNode
                            spEdges.add((lesserVal, greaterVal))
                            stackList.append((neighbor, distArray[neighbor]))
                exploreStack()

            exploreStack()
            return spEdges

        graphConstructed = buildGraph(q)
        shortestDistances = dijkstra(p, graphConstructed)
        spEdgeSet = findSPEdges(graphConstructed, shortestDistances, p)
        resultList = []

        for index in range(len(q)):
            x, y = q[index][0], q[index][1]
            lowNode, highNode = (x, y) if x <= y else (y, x)
            isInSP = (lowNode, highNode) in spEdgeSet
            resultList.append(isInSP)

        return resultList