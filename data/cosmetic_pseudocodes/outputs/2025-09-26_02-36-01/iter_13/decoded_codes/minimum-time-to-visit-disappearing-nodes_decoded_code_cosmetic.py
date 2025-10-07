from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        def enqueue(heap, item):
            idx = len(heap)
            heap.append(item)
            while idx > 0:
                parent = (idx - 1) // 2
                if heap[parent][0] <= heap[idx][0]:
                    break
                heap[parent], heap[idx] = heap[idx], heap[parent]
                idx = parent

        def dequeue(heap):
            if not heap:
                return None
            result = heap[0]
            last = heap.pop()
            if not heap:
                return result
            heap[0] = last
            idx = 0
            length = len(heap)
            while True:
                left = 2 * idx + 1
                right = 2 * idx + 2
                smallest = idx
                if left < length and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < length and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest == idx:
                    break
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                idx = smallest
            return result

        def makeGraph(edgeList):
            graphMap = defaultdict(list)
            for fromNode, toNode, edgeLength in edgeList:
                graphMap[fromNode].append((toNode, edgeLength))
                graphMap[toNode].append((fromNode, edgeLength))
            return graphMap

        def recursiveProcess(queue, distArray, graphObj, disappearArr):
            if not queue:
                return
            currEntry = dequeue(queue)
            if currEntry is None:
                return
            distCurr, nodeCurr = currEntry
            if distCurr >= disappearArr[nodeCurr]:
                recursiveProcess(queue, distArray, graphObj, disappearArr)
                return
            if distCurr > distArray[nodeCurr]:
                recursiveProcess(queue, distArray, graphObj, disappearArr)
                return
            neighbors = graphObj[nodeCurr]

            def helperLoop(idx):
                if idx >= len(neighbors):
                    return
                neighborNode, lengthEdge = neighbors[idx]
                newDist = distCurr + lengthEdge
                if newDist < distArray[neighborNode] and newDist < disappearArr[neighborNode]:
                    distArray[neighborNode] = newDist
                    enqueue(queue, (newDist, neighborNode))
                helperLoop(idx + 1)

            helperLoop(0)
            recursiveProcess(queue, distArray, graphObj, disappearArr)

        alphaGraph = makeGraph(edges)
        dist = [inf] * n
        dist[0] = 0
        heap = []
        enqueue(heap, (0, 0))
        recursiveProcess(heap, dist, alphaGraph, disappear)

        answer = [-1] * n
        for idx in range(n):
            if dist[idx] < disappear[idx]:
                answer[idx] = dist[idx]

        return answer