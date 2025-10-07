class Solution:
    def minimumTime(self, count, links, vanish):
        def pushHeap(heapList, item):
            index = len(heapList)
            heapList.append(item)
            while index > 0:
                parentIdx = (index - 2) // 2
                if HEAPCOMPARE(heapList[parentIdx], heapList[index]) > 0:
                    heapList[parentIdx], heapList[index] = heapList[index], heapList[parentIdx]
                    index = parentIdx
                else:
                    break

        def popHeap(heapList):
            if len(heapList) == 0:
                return None
            firstItem = heapList[0]
            lastItem = heapList.pop()
            if len(heapList) == 0:
                return firstItem
            heapList[0] = lastItem
            idx = 0
            lenHeap = len(heapList)
            while True:
                leftChild = 2 * idx + 1
                rightChild = leftChild + 1
                smallest = idx
                if leftChild < lenHeap and HEAPCOMPARE(heapList[leftChild], heapList[smallest]) < 0:
                    smallest = leftChild
                if rightChild < lenHeap and HEAPCOMPARE(heapList[rightChild], heapList[smallest]) < 0:
                    smallest = rightChild
                if smallest != idx:
                    heapList[idx], heapList[smallest] = heapList[smallest], heapList[idx]
                    idx = smallest
                else:
                    break
            return firstItem

        def HEAPCOMPARE(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                return 0

        def dfsBuildGraph(index, maxIndex, edgeArray):
            def helper(i, currentGraph):
                if i >= maxIndex:
                    return currentGraph
                nodeX, nodeY, pathLen = edgeArray[i]
                if nodeX not in currentGraph:
                    currentGraph[nodeX] = []
                if nodeY not in currentGraph:
                    currentGraph[nodeY] = []
                currentGraph[nodeX].append((nodeY, pathLen))
                currentGraph[nodeY].append((nodeX, pathLen))
                return helper(i + 1, currentGraph)
            return helper(index, {})

        topoGraph = dfsBuildGraph(0, len(links), links)
        infVal = 1_000_000_000

        costArray = [infVal] * count
        costArray[0] = 0

        heapData = [(0, 0)]

        def processHeap(heap, distancesMap, disappearList, graphMap):
            if len(heap) == 0:
                return
            headPair = popHeap(heap)
            distCurr, nodeCurr = headPair
            if not (distCurr < disappearList[nodeCurr]):
                processHeap(heap, distancesMap, disappearList, graphMap)
                return
            if not (distCurr < distancesMap[nodeCurr]):
                processHeap(heap, distancesMap, disappearList, graphMap)
                return
            adjList = graphMap[nodeCurr]
            idxAdj = len(adjList) - 1
            while idxAdj >= 0:
                nextNode, edgeDist = adjList[idxAdj]
                proposedDist = distCurr + edgeDist
                if proposedDist < distancesMap[nextNode] and proposedDist < disappearList[nextNode]:
                    distancesMap[nextNode] = proposedDist
                    pushHeap(heap, (proposedDist, nextNode))
                idxAdj -= 1
            processHeap(heap, distancesMap, disappearList, graphMap)

        processHeap(heapData, costArray, vanish, topoGraph)

        answerArray = []
        countIter = 0
        while countIter < count:
            if costArray[countIter] < vanish[countIter]:
                answerArray.append(costArray[countIter])
            else:
                answerArray.append(-1)
            countIter += 1

        return answerArray