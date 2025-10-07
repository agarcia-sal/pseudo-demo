class Solution:
    def findAnswer(self, n, edges):
        def enqueue(heap, item):
            heap.append(item)
            idx = len(heap) - 1
            while idx > 0:
                parent_idx = (idx - 1) // 2
                if parent_idx < 0 or heap[parent_idx][0] <= heap[idx][0]:
                    break
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                idx = parent_idx

        def dequeue(heap):
            if len(heap) == 0:
                return None
            root = heap[0]
            last_idx = len(heap) - 1
            heap[0] = heap[last_idx]
            heap.pop()
            idx = 0
            length = len(heap)
            while True:
                left_idx = 2 * idx + 1
                right_idx = 2 * idx + 2
                smallest_idx = idx
                if left_idx < length and heap[left_idx][0] < heap[smallest_idx][0]:
                    smallest_idx = left_idx
                if right_idx < length and heap[right_idx][0] < heap[smallest_idx][0]:
                    smallest_idx = right_idx
                if smallest_idx == idx:
                    break
                heap[idx], heap[smallest_idx] = heap[smallest_idx], heap[idx]
                idx = smallest_idx
            return root

        adjMap = dict()
        for edge_triple in edges:
            x, y, z = edge_triple
            if x not in adjMap:
                adjMap[x] = []
            if y not in adjMap:
                adjMap[y] = []
            adjMap[x].append((y, z))
            adjMap[y].append((x, z))

        INF = float('inf')
        distances = [INF] * n
        distances[0] = 0

        priorityQueue = []
        enqueue(priorityQueue, (distances[0], 0))

        def dijkstraIter():
            if len(priorityQueue) == 0:
                return False
            current_tuple = dequeue(priorityQueue)
            currDist, currNode = current_tuple
            if currDist > distances[currNode]:
                return True
            for nextNode, edgeCost in adjMap.get(currNode, ()):
                newDist = currDist + edgeCost
                if newDist < distances[nextNode]:
                    distances[nextNode] = newDist
                    enqueue(priorityQueue, (newDist, nextNode))
            return True

        while dijkstraIter():
            pass

        shortestEdgeSet = set()
        stackQ = [(n - 1, distances[n - 1])]
        visitedFlags = [False] * n

        def dfsProcess():
            if len(stackQ) == 0:
                return False
            currentNode, currentDist = stackQ.pop()
            if visitedFlags[currentNode]:
                return True
            visitedFlags[currentNode] = True
            for adjacentNode, weightEdge in adjMap.get(currentNode, ()):
                distSum = distances[adjacentNode] + weightEdge
                if currentDist == distSum:
                    lowVal, highVal = (adjacentNode, currentNode) if adjacentNode < currentNode else (currentNode, adjacentNode)
                    shortestEdgeSet.add((lowVal, highVal))
                    stackQ.append((adjacentNode, distances[adjacentNode]))
            return True

        while dfsProcess():
            pass

        resultArray = []
        for edgeIndex in range(len(edges) - 1, -1, -1):
            eU, eV, _ = edges[edgeIndex]
            lowE, highE = (eV, eU) if eV < eU else (eU, eV)
            containsFlag = (lowE, highE) in shortestEdgeSet
            resultArray.insert(0, containsFlag)

        return resultArray