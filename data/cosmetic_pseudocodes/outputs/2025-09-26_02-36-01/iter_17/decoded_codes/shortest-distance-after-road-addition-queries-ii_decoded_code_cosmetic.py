class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        connectionMap = {i: [] for i in range(n)}
        for edgeIndex in range(n - 1):
            connectionMap[edgeIndex].append((edgeIndex + 1, 1))

        def dijkstra():
            distances = [float('inf')] * n
            distances[0] = 0
            heapQueue = [(0, 0)]

            def heapPopMin(queue):
                minIdx = 0
                for idx in range(1, len(queue)):
                    if queue[idx][0] < queue[minIdx][0]:
                        minIdx = idx
                return queue.pop(minIdx)

            def heapPush(queue, element):
                queue.append(element)

            while heapQueue:
                currentDistance, currentVertex = heapPopMin(heapQueue)
                if distances[currentVertex] < currentDistance:
                    continue
                for adjNode, edgeCost in connectionMap[currentVertex]:
                    candidateDistance = currentDistance + edgeCost
                    if candidateDistance < distances[adjNode]:
                        distances[adjNode] = candidateDistance
                        heapPush(heapQueue, (candidateDistance, adjNode))

            return distances[n - 1]

        answerList = []
        queryIdx = 0
        while True:
            if queryIdx >= len(queries):
                break
            fromNode, toNode = queries[queryIdx]
            connectionMap[fromNode].append((toNode, 1))
            answerList.append(dijkstra())
            queryIdx += 1

        return answerList