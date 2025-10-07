from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        def insertHeap(h, item):
            def heapifyUp(idx):
                if idx == 0:
                    return
                p = (idx - 1) // 2
                if h[p][0] > h[idx][0]:
                    h[p], h[idx] = h[idx], h[p]
                    heapifyUp(p)
            h.append(item)
            heapifyUp(len(h) - 1)

        def extractMin(h):
            if len(h) == 0:
                return (-1, -1)
            ret = h[0]
            last_item = h.pop()
            if len(h) == 0:
                return ret
            h[0] = last_item
            def heapifyDown(idx):
                l = 2 * idx + 1
                r = 2 * idx + 2
                smallest = idx
                if l < len(h) and h[l][0] < h[smallest][0]:
                    smallest = l
                if r < len(h) and h[r][0] < h[smallest][0]:
                    smallest = r
                if smallest != idx:
                    h[idx], h[smallest] = h[smallest], h[idx]
                    heapifyDown(smallest)
            heapifyDown(0)
            return ret

        mappingGraph = defaultdict(list)
        def buildGraph(idx):
            if idx == len(edges):
                return
            a, b, c = edges[idx]
            mappingGraph[a].append((b, c))
            mappingGraph[b].append((a, c))
            buildGraph(idx + 1)
        buildGraph(0)

        distArr = [inf] * n
        distArr[0] = 0

        heapQueue = [(0, 0)]

        def loopProcess():
            if len(heapQueue) <= 0:
                return
            curDist, curNode = extractMin(heapQueue)
            if curDist >= disappear[curNode]:
                loopProcess()
                return
            if curDist > distArr[curNode]:
                loopProcess()
                return
            def visitNeighbors(idxNeighbor):
                if idxNeighbor == len(mappingGraph[curNode]):
                    return
                nb, ln = mappingGraph[curNode][idxNeighbor]
                totalDist = curDist + ln
                if totalDist < distArr[nb] and totalDist < disappear[nb]:
                    distArr[nb] = totalDist
                    insertHeap(heapQueue, (totalDist, nb))
                visitNeighbors(idxNeighbor + 1)
            visitNeighbors(0)
            loopProcess()
        loopProcess()

        answerArr = [-1] * n
        def fillAnswer(indexX):
            if indexX >= n:
                return
            if distArr[indexX] < disappear[indexX]:
                answerArr[indexX] = distArr[indexX]
            fillAnswer(indexX + 1)
        fillAnswer(0)

        return answerArr