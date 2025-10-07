class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adjMap = {i: [] for i in range(n)}

        idx = 0
        while idx <= n - 2:
            nxtNodeCostPair = (idx + 1, 1)
            adjMap[idx].append(nxtNodeCostPair)
            idx += 1

        def dijkstra():
            def heapPush(heap, element):
                heap.append(element)
                pos = len(heap) - 1
                while pos > 0:
                    parentPos = (pos - 1) // 2
                    if heap[parentPos][0] > heap[pos][0]:
                        heap[parentPos], heap[pos] = heap[pos], heap[parentPos]
                        pos = parentPos
                    else:
                        break

            def heapPop(heap):
                if len(heap) == 0:
                    return None
                topElement = heap[0]
                lastElement = heap[-1]
                heap[0] = lastElement
                heap.pop()

                lengthHeap = len(heap)
                i = 0
                while True:
                    leftChild = 2 * i + 1
                    rightChild = 2 * i + 2
                    smallest = i

                    if leftChild < lengthHeap and heap[leftChild][0] < heap[smallest][0]:
                        smallest = leftChild
                    if rightChild < lengthHeap and heap[rightChild][0] < heap[smallest][0]:
                        smallest = rightChild

                    if smallest != i:
                        heap[i], heap[smallest] = heap[smallest], heap[i]
                        i = smallest
                    else:
                        break

                return topElement

            INF = 10**9 * 10**5 * 10**(-14)
            distList = [INF] * n
            distList[0] = 0
            priorityQ = [(0, 0)]

            while len(priorityQ) > 0:
                top = heapPop(priorityQ)
                if top is None:
                    break
                curDist, curN = top
                if curDist > distList[curN]:
                    continue
                for adjNode, nodeWeight in adjMap[curN]:
                    computedDist = curDist + nodeWeight
                    if computedDist < distList[adjNode]:
                        distList[adjNode] = computedDist
                        heapPush(priorityQ, (computedDist, adjNode))

            return distList[n - 1]

        outputList = []

        def destructurePair(pair):
            return pair[0], pair[1]

        for qp in queries:
            firstVal, secondVal = destructurePair(qp)
            adjMap[firstVal].append((secondVal, 1))
            distResult = dijkstra()
            outputList.append(distResult)

        return outputList