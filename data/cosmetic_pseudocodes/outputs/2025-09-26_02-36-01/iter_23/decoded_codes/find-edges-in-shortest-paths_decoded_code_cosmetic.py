from collections import defaultdict
from typing import List, Tuple

class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        def pushHeap(arr: List[Tuple[int, int]], item: Tuple[int, int]) -> None:
            idx = len(arr)
            arr.append(item)
            while idx > 0:
                parent = (idx - 1) // 2
                if arr[parent][0] > arr[idx][0]:
                    arr[parent], arr[idx] = arr[idx], arr[parent]
                    idx = parent
                else:
                    break

        def popHeap(arr: List[Tuple[int, int]]) -> Tuple[int, int] or None:
            if len(arr) == 0:
                return None
            root = arr[0]
            endElem = arr.pop()
            if len(arr) == 0:
                return root
            arr[0] = endElem
            idx = 0
            length = len(arr)
            while True:
                leftChild = 2 * idx + 1
                rightChild = 2 * idx + 2
                swapIdx = idx
                if leftChild < length and arr[leftChild][0] < arr[swapIdx][0]:
                    swapIdx = leftChild
                if rightChild < length and arr[rightChild][0] < arr[swapIdx][0]:
                    swapIdx = rightChild
                if swapIdx == idx:
                    break
                arr[idx], arr[swapIdx] = arr[swapIdx], arr[idx]
                idx = swapIdx
            return root

        def buildGraph(edgeList: List[Tuple[int, int, int]]) -> defaultdict:
            graph = defaultdict(list)

            def recurBuild(idx: int) -> None:
                if idx == len(edgeList):
                    return
                a, b, c = edgeList[idx]
                graph[a].append((b, c))
                graph[b].append((a, c))
                recurBuild(idx + 1)

            recurBuild(0)
            return graph

        graphMap = buildGraph(edges)
        maxVal = (1 << 30) + (1 << 15) - 123456
        distArr = [maxVal] * n
        distArr[0] = 0

        def relaxAndPush(pQ: List[Tuple[int, int]], node: int, distVal: int) -> None:
            pushHeap(pQ, (distVal, node))

        heapQueue: List[Tuple[int, int]] = []
        relaxAndPush(heapQueue, 0, 0)

        def dijkstraLoop() -> None:
            if len(heapQueue) == 0:
                return
            currPair = popHeap(heapQueue)
            if currPair is None:
                return
            curDist, currNode = currPair

            if curDist > distArr[currNode]:
                dijkstraLoop()
                return

            def neighborsLoop(idxN: int) -> None:
                if idxN == len(graphMap[currNode]):
                    dijkstraLoop()
                    return
                nd, wgt = graphMap[currNode][idxN]
                sumDist = curDist + wgt
                if sumDist < distArr[nd]:
                    distArr[nd] = sumDist
                    relaxAndPush(heapQueue, nd, sumDist)
                neighborsLoop(idxN + 1)

            neighborsLoop(0)

        dijkstraLoop()

        spEdges = set()
        stackList = [(n - 1, distArr[n - 1])]
        visitedArr = [False] * n

        def stackProc() -> None:
            if len(stackList) == 0:
                return
            currU, currD = stackList.pop()
            if visitedArr[currU]:
                stackProc()
                return
            visitedArr[currU] = True

            def innerCheck(indexC: int) -> None:
                if indexC == len(graphMap[currU]):
                    stackProc()
                    return
                nbV, nbW = graphMap[currU][indexC]
                if currD == distArr[nbV] + nbW:
                    lowNode, highNode = (currU, nbV) if currU < nbV else (nbV, currU)
                    spEdges.add((lowNode, highNode))
                    stackList.append((nbV, distArr[nbV]))
                innerCheck(indexC + 1)

            innerCheck(0)

        stackProc()

        retList: List[bool] = []

        def finalCheck(idxE: int) -> None:
            if idxE == len(edges):
                return
            u1, v1, _ = edges[idxE]
            lowVal1, highVal1 = (u1, v1) if u1 < v1 else (v1, u1)
            containsEdge = (lowVal1, highVal1) in spEdges
            retList.append(containsEdge)
            finalCheck(idxE + 1)

        finalCheck(0)

        return retList