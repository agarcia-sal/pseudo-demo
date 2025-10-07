from typing import List, Tuple


class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        graph = {i: [] for i in range(n)}

        for a, b, c in edges:
            graph[a].append((b, c))
            graph[b].append((a, c))

        dist = [float('inf')] * n
        dist[0] = 0

        heapList = [(0, 0)]  # (distance, node)

        def popMin(heap: List[Tuple[int, int]]) -> Tuple[int, int]:
            idx = 0
            for i in range(1, len(heap)):
                if heap[i][0] < heap[idx][0]:
                    idx = i
            item = heap[idx]
            # Remove element at idx
            heap[idx] = heap[-1]
            heap.pop()
            return item

        def pushHeap(heap: List[Tuple[int, int]], item: Tuple[int, int]) -> None:
            heap.append(item)

        while heapList:
            currDist, node = popMin(heapList)
            if currDist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                newDist = currDist + weight
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    pushHeap(heapList, (newDist, neighbor))

        pathEdges = set()
        stackList = [(n - 1, dist[n - 1])]
        visitFlags = [False] * n

        while stackList:
            currNode, currDistVal = stackList.pop()
            if visitFlags[currNode]:
                continue
            visitFlags[currNode] = True
            for adjNode, adjWeight in graph[currNode]:
                if currDistVal == dist[adjNode] + adjWeight:
                    aVal, bVal = currNode, adjNode
                    if aVal > bVal:
                        aVal, bVal = bVal, aVal
                    pathEdges.add((aVal, bVal))
                    stackList.append((adjNode, dist[adjNode]))

        resultList = []
        for firstNode, secondNode, _ in edges:
            mA, mB = firstNode, secondNode
            if mA > mB:
                mA, mB = mB, mA
            resultList.append((mA, mB) in pathEdges)

        return resultList