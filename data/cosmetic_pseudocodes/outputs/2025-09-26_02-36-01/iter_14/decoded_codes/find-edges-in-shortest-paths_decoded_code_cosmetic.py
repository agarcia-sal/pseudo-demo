from collections import defaultdict
from math import inf

class Solution:
    def findAnswer(self, n, edges):
        def InsertHeapElement(heap, elem):
            index = len(heap)
            heap.append(elem)
            while index > 0:
                parent = (index - 1) // 2
                if heap[parent][0] <= heap[index][0]:
                    break
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent

        def PopHeapElement(heap):
            if len(heap) == 0:
                return None
            result = heap[0]
            lastElem = heap.pop()
            if len(heap) == 0:
                return result
            heap[0] = lastElem
            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < len(heap) and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < len(heap) and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            return result

        adjacencyMap = defaultdict(list)
        for x, y, z in edges:
            adjacencyMap[x].append((y, z))
            adjacencyMap[y].append((x, z))

        distances = [inf] * n
        distances[0] = 0
        priorityQueue = [(0, 0)]

        while len(priorityQueue) > 0:
            currDist, node = PopHeapElement(priorityQueue)
            if currDist > distances[node]:
                continue
            for neighbor, weight in adjacencyMap[node]:
                tempDist = currDist + weight
                if tempDist < distances[neighbor]:
                    distances[neighbor] = tempDist
                    InsertHeapElement(priorityQueue, (tempDist, neighbor))

        resultEdges = set()
        traversalStack = [(n - 1, distances[n - 1])]
        seenNodes = [False] * n

        while len(traversalStack) > 0:
            currNode, currDist = traversalStack.pop()
            if seenNodes[currNode]:
                continue
            seenNodes[currNode] = True
            for adjNode, wgt in adjacencyMap[currNode]:
                if currDist == distances[adjNode] + wgt:
                    edgePair = (min(currNode, adjNode), max(currNode, adjNode))
                    if edgePair not in resultEdges:
                        resultEdges.add(edgePair)
                        traversalStack.append((adjNode, distances[adjNode]))

        outputList = []
        for a, b, _ in edges:
            outputList.append((min(a, b), max(a, b)) in resultEdges)
        return outputList