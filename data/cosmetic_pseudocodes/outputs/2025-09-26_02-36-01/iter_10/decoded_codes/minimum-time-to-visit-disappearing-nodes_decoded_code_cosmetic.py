from collections import defaultdict
from typing import List, Tuple, Optional

class Solution:
    def minimumTime(self, n: int, edges: List[Tuple[int, int, int]], disappear: List[int]) -> List[int]:

        def InsertHeapElement(heap: List[Tuple[int, int]], val: Tuple[int, int]) -> None:
            heap.append(val)
            pos = len(heap) - 1
            while pos > 0:
                parent = (pos - 1) // 2
                if heap[parent][0] > heap[pos][0]:
                    heap[parent], heap[pos] = heap[pos], heap[parent]
                    pos = parent
                else:
                    break

        def ExtractHeapMin(heap: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
            if not heap:
                return None
            rootVal = heap[0]
            lastVal = heap.pop()
            if not heap:
                return rootVal
            heap[0] = lastVal
            idx = 0
            sz = len(heap)
            while True:
                leftIdx = 2 * idx + 1
                rightIdx = 2 * idx + 2
                smallest = idx
                if leftIdx < sz and heap[leftIdx][0] < heap[smallest][0]:
                    smallest = leftIdx
                if rightIdx < sz and heap[rightIdx][0] < heap[smallest][0]:
                    smallest = rightIdx
                if smallest == idx:
                    break
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                idx = smallest
            return rootVal

        adjList = defaultdict(list)

        def processEdges(pos: int) -> None:
            if pos == len(edges):
                return
            a, b, w = edges[pos]
            adjList[a].append((b, w))
            adjList[b].append((a, w))
            processEdges(pos + 1)

        processEdges(0)

        INF = 10**9 + 7
        distArray = [INF] * n
        distArray[0] = 0

        heapList: List[Tuple[int, int]] = []
        InsertHeapElement(heapList, (0, 0))

        def DijkstraLoop() -> None:
            while heapList:
                currentPair = ExtractHeapMin(heapList)
                if currentPair is None:
                    break
                curDist, curNode = currentPair

                if curDist >= disappear[curNode]:
                    continue

                if curDist > distArray[curNode]:
                    continue

                for neigh, leng in adjList[curNode]:
                    computedDist = curDist + leng
                    if computedDist < distArray[neigh] and computedDist < disappear[neigh]:
                        distArray[neigh] = computedDist
                        InsertHeapElement(heapList, (computedDist, neigh))

        DijkstraLoop()

        outputList = [0] * n
        posCounter = 0
        # buildResultLoop
        while posCounter < n:
            if distArray[posCounter] < disappear[posCounter]:
                outputList[posCounter] = distArray[posCounter]
            else:
                outputList[posCounter] = -1
            posCounter += 1
        # endBuildResultLoop

        return outputList