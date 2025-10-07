class Solution:
    def findAnswer(self, n, edges):
        def minTupleExtract(heap):
            idx = 0
            minIdx = 0
            lenHeap = len(heap)
            while idx < lenHeap:
                if heap[idx][0] < heap[minIdx][0]:
                    minIdx = idx
                idx += 1
            result = heap[minIdx]
            heap[minIdx], heap[-1] = heap[-1], heap[minIdx]
            heap.pop()
            parent = 0
            size = len(heap)
            while True:
                leftChild = 2 * parent + 1
                rightChild = leftChild + 1
                smallest = parent
                if leftChild < size and heap[leftChild][0] < heap[smallest][0]:
                    smallest = leftChild
                if rightChild < size and heap[rightChild][0] < heap[smallest][0]:
                    smallest = rightChild
                if smallest == parent:
                    break
                heap[parent], heap[smallest] = heap[smallest], heap[parent]
                parent = smallest
            return result

        def heapPush(heap, val):
            heap.append(val)
            idx = len(heap) - 1
            while idx > 0:
                parent = (idx - 1) // 2
                if heap[parent][0] <= heap[idx][0]:
                    break
                heap[parent], heap[idx] = heap[idx], heap[parent]
                idx = parent

        adjacencyMap = {}
        each_key = 0
        while each_key < n:
            adjacencyMap[each_key] = []
            each_key += 1

        index_i = 0
        while index_i < len(edges):
            edgeTriple = edges[index_i]
            nodeP, nodeQ, weightR = edgeTriple
            adjacencyMap[nodeP].append((nodeQ, weightR))
            adjacencyMap[nodeQ].append((nodeP, weightR))
            index_i += 1

        distList = []
        fillPos = 0
        INF = 10 ** 9
        while fillPos < n:
            distList.append(INF)
            fillPos += 1

        distList[0] = 0

        priorityQueue = [(0, 0)]

        def pqHasElements(pq):
            return len(pq) > 0

        while pqHasElements(priorityQueue):
            currD, currNode = minTupleExtract(priorityQueue)
            if currD > distList[currNode]:
                continue
            idx_j = 0
            neighList = adjacencyMap[currNode]
            while idx_j < len(neighList):
                neighbor, weightVal = neighList[idx_j]
                tentative = currD + weightVal
                if tentative < distList[neighbor]:
                    distList[neighbor] = tentative
                    heapPush(priorityQueue, (tentative, neighbor))
                idx_j += 1

        edgeSet = set()

        stackList = [(n - 1, distList[n - 1])]
        visitedList = []
        idx_v = 0
        while idx_v < n:
            visitedList.append(False)
            idx_v += 1

        def stackNotEmpty(stk):
            return len(stk) > 0

        while stackNotEmpty(stackList):
            nodeX, distX = stackList[-1]
            stackList.pop()
            if visitedList[nodeX]:
                continue
            visitedList[nodeX] = True
            idx_k = 0
            nghList2 = adjacencyMap[nodeX]
            while idx_k < len(nghList2):
                nbrNode, wgt = nghList2[idx_k]
                if distX == distList[nbrNode] + wgt:
                    if nodeX < nbrNode:
                        edgeSet |= {(nodeX, nbrNode)}
                    else:
                        edgeSet |= {(nbrNode, nodeX)}
                    stackList.append((nbrNode, distList[nbrNode]))
                idx_k += 1

        resultArr = []
        idx_m = 0
        while idx_m < len(edges):
            x1, x2, _ = edges[idx_m]
            if x1 < x2:
                edgeTuple = (x1, x2)
            else:
                edgeTuple = (x2, x1)
            resultArr.append(edgeTuple in edgeSet)
            idx_m += 1

        return resultArr