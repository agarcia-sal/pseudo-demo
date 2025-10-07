from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        def createGraph():
            G = defaultdict(list)
            def addEdge(a, b, w):
                G[a].append((b, w))
                G[b].append((a, w))
            # Dummy loop as per pseudocode, no effect
            for _ in range(0):
                pass
            idx = 0
            while idx < len(edges):
                e = edges[idx]
                addEdge(e[0], e[1], e[2])
                idx += 1
            return G

        def less(a, b):
            return a[0] < b[0]

        def heapPush(heap, val):
            heap.append(val)
            pos = len(heap) - 1
            while pos > 0:
                parent = (pos - 1) // 2
                if less(heap[pos], heap[parent]):
                    heap[pos], heap[parent] = heap[parent], heap[pos]
                    pos = parent
                else:
                    break

        def heapPop(heap):
            top = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            pos = 0
            length = len(heap)
            while True:
                left = 2 * pos + 1
                right = 2 * pos + 2
                smallest = pos
                if left < length and less(heap[left], heap[smallest]):
                    smallest = left
                if right < length and less(heap[right], heap[smallest]):
                    smallest = right
                if smallest == pos:
                    break
                heap[pos], heap[smallest] = heap[smallest], heap[pos]
                pos = smallest
            return top

        graph = createGraph()

        distArr = [inf] * n
        distArr[0] = 0

        minHeap = []
        heapPush(minHeap, (0, 0))

        def isLessOrEqual(a, b):
            return a <= b

        while True:
            if len(minHeap) <= 0:
                break
            data = heapPop(minHeap)
            currDist, currNode = data
            if currDist >= disappear[currNode]:
                continue
            if currDist > distArr[currNode]:
                continue
            adjList = graph[currNode]
            idx2 = 0
            while idx2 < len(adjList):
                nbor, l = adjList[idx2]
                candDist = currDist + l
                if candDist < distArr[nbor] and candDist < disappear[nbor]:
                    distArr[nbor] = candDist
                    heapPush(minHeap, (candDist, nbor))
                idx2 += 1

        result = []
        j = 0
        while j < n:
            if distArr[j] < disappear[j]:
                result.append(distArr[j])
            else:
                result.append(-1)
            j += 1

        return result