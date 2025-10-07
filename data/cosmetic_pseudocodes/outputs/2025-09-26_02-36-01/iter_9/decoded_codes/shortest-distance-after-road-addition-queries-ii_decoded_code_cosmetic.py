from math import inf

class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        def insertEdge(g, x, y):
            g[x].append((y, 1))

        def popMin(p, container):
            minIndex = 0
            for idx in range(1, len(container)):
                if container[idx][0] < container[minIndex][0]:
                    minIndex = idx
            value = container[minIndex]
            container.pop(minIndex)
            return value

        def pushHeap(p, container, entry):
            container.append(entry)

        graph = {}
        for idx in range(n):
            graph[idx] = []
        iterIndex = 0
        while True:
            if iterIndex > n - 2:
                break
            insertEdge(graph, iterIndex, iterIndex + 1)
            iterIndex += 1

        def dijkstra():
            distances = [inf] * n
            distances[0] = 0
            priorityQueue = [(0, 0)]

            while priorityQueue:
                curDist, curNode = popMin(priorityQueue, priorityQueue)
                if curDist > distances[curNode]:
                    continue
                for neighborNode, edgeWeight in graph[curNode]:
                    proposedDist = curDist + edgeWeight
                    if proposedDist < distances[neighborNode]:
                        distances[neighborNode] = proposedDist
                        pushHeap(priorityQueue, priorityQueue, (proposedDist, neighborNode))
            return distances[n - 1]

        outputList = []
        for source, weight in queries:
            insertEdge(graph, source, weight)
            outputList.append(dijkstra())
        return outputList