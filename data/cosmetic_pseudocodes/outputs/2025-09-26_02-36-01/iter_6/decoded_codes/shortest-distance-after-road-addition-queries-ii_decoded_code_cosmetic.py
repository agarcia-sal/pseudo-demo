class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        def minHeapPush(heap, val):
            idx = len(heap)
            heap.append(val)
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if heap[parentIdx][0] <= heap[idx][0]:
                    break
                heap[parentIdx], heap[idx] = heap[idx], heap[parentIdx]
                idx = parentIdx

        def minHeapPop(heap):
            retVal = heap[0]
            lastIdx = len(heap) - 1
            heap[0] = heap[lastIdx]
            heap.pop()

            currentIdx = 0
            length = len(heap)
            while True:
                leftIdx = currentIdx * 2 + 1
                rightIdx = currentIdx * 2 + 2
                if leftIdx >= length:
                    break
                smallChildIdx = leftIdx
                if rightIdx < length and heap[rightIdx][0] < heap[leftIdx][0]:
                    smallChildIdx = rightIdx
                if heap[currentIdx][0] <= heap[smallChildIdx][0]:
                    break
                heap[currentIdx], heap[smallChildIdx] = heap[smallChildIdx], heap[currentIdx]
                currentIdx = smallChildIdx

            return retVal

        adjacencyMap = {}

        def initializeGraph(limit):
            def addEdge(adj, fromNode, toNode, w):
                if fromNode not in adj:
                    adj[fromNode] = []
                adj[fromNode].append((toNode, w))

            for q in range(limit - 1, -1, -1):
                addEdge(adjacencyMap, q, q + 1, 1)

        def dijkstra():
            INF = 1_000_000_000
            distances = [INF] * n
            distances[0] = 0
            priorityQueue = [(0, 0)]

            while priorityQueue:
                distVal, nodeVal = minHeapPop(priorityQueue)

                if distVal > distances[nodeVal]:
                    continue

                if nodeVal in adjacencyMap:
                    for neighborNode, weightEdge in adjacencyMap[nodeVal]:
                        altDist = distVal + weightEdge
                        if altDist < distances[neighborNode]:
                            distances[neighborNode] = altDist
                            minHeapPush(priorityQueue, (altDist, neighborNode))

            return distances[n - 1]

        initializeGraph(n)

        outputCollector = []

        def processQueries(recQueries, index, count):
            if index >= count:
                return
            startNode, endNode = recQueries[index]
            if startNode not in adjacencyMap:
                adjacencyMap[startNode] = []
            adjacencyMap[startNode].append((endNode, 1))
            outputCollector.append(dijkstra())
            processQueries(recQueries, index + 1, count)

        processQueries(queries, 0, len(queries))

        return outputCollector