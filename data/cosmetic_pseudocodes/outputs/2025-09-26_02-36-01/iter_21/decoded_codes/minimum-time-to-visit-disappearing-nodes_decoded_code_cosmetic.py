from collections import defaultdict

class Solution:
    def minimumTime(self, n, edges, disappear):
        def insertHeap(heapList, item):
            heapList.append(item)
            index = len(heapList) - 1

            while index > 0:
                parentIdx = (index - 1) // 2
                if heapList[parentIdx][0] > heapList[index][0]:
                    heapList[parentIdx], heapList[index] = heapList[index], heapList[parentIdx]
                    index = parentIdx
                else:
                    break
            return heapList

        def popMin(heapList):
            if len(heapList) == 0:
                return None, None, heapList
            firstItem = heapList[0]
            lastItem = heapList[-1]
            heapList = heapList[:-1]
            if len(heapList) > 0:
                heapList[0] = lastItem
                idx = 0
                while True:
                    leftChild = idx * 2 + 1
                    rightChild = idx * 2 + 2
                    smallest = idx

                    if leftChild < len(heapList) and heapList[leftChild][0] < heapList[smallest][0]:
                        smallest = leftChild
                    if rightChild < len(heapList) and heapList[rightChild][0] < heapList[smallest][0]:
                        smallest = rightChild
                    if smallest == idx:
                        break
                    heapList[idx], heapList[smallest] = heapList[smallest], heapList[idx]
                    idx = smallest
            return firstItem[0], firstItem[1], heapList

        def buildGraph(edgeList):
            graphMap = defaultdict(list)

            def processEdge(u, v, w):
                graphMap[u].append((v, w))
                graphMap[v].append((u, w))

            idx = 0
            while idx < len(edgeList):
                e = edgeList[idx]
                processEdge(e[0], e[1], e[2])
                idx += 1
            return graphMap

        graph = buildGraph(edges)
        INF = 10**10
        distList = [INF] * n
        distList[0] = 0

        heapStructure = [(0, 0)]

        def dijkstraLoop(heapCurrent, distCurrent):
            if len(heapCurrent) == 0:
                return distCurrent

            heapDist, heapNode, heapCurrent = popMin(heapCurrent)

            if heapDist is None:
                return distCurrent

            if heapDist >= disappear[heapNode]:
                return dijkstraLoop(heapCurrent, distCurrent)

            if heapDist > distCurrent[heapNode]:
                return dijkstraLoop(heapCurrent, distCurrent)

            def neighborScan(idx):
                if idx >= len(graph[heapNode]):
                    return
                nbrNode, nbrLen = graph[heapNode][idx]
                newDist = heapDist + nbrLen

                if newDist < distCurrent[nbrNode] and newDist < disappear[nbrNode]:
                    distCurrent[nbrNode] = newDist
                    nonlocal heapCurrent
                    heapCurrent = insertHeap(heapCurrent, (newDist, nbrNode))
                neighborScan(idx + 1)

            neighborScan(0)
            return dijkstraLoop(heapCurrent, distCurrent)

        distances = dijkstraLoop(heapStructure, distList)
        outputResult = [-1] * n

        def fillResult(index):
            if index >= n:
                return
            if distances[index] < disappear[index]:
                outputResult[index] = distances[index]
            fillResult(index + 1)

        fillResult(0)
        return outputResult