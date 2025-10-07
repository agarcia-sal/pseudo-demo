class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adjacencyMap = {i: [] for i in range(n)}
        indexCounter = 0
        while True:
            if indexCounter > n - 2:
                break
            link = (indexCounter + 1, 1)
            adjacencyMap[indexCounter].append(link)
            indexCounter += 1

        def dijkstra():
            distances = [float('inf')] * n
            distances[0] = 0
            priorityQueue = [(0, 0)]

            def siftDown(queue):
                start = 0
                while True:
                    leftChild = 2 * start + 1
                    rightChild = 2 * start + 2
                    smallest = start
                    if leftChild < len(queue) and queue[leftChild][0] < queue[smallest][0]:
                        smallest = leftChild
                    if rightChild < len(queue) and queue[rightChild][0] < queue[smallest][0]:
                        smallest = rightChild
                    if smallest == start:
                        break
                    queue[start], queue[smallest] = queue[smallest], queue[start]
                    start = smallest

            def pushHeap(queue, item):
                queue.append(item)
                idx = len(queue) - 1
                while idx > 0:
                    parent = (idx - 1) // 2
                    if queue[parent][0] <= queue[idx][0]:
                        break
                    queue[parent], queue[idx] = queue[idx], queue[parent]
                    idx = parent

            def popHeap(queue):
                initial = queue[0]
                lastItem = queue.pop()
                if queue:
                    queue[0] = lastItem
                    start = 0
                    while True:
                        leftChild = 2 * start + 1
                        rightChild = 2 * start + 2
                        smallest = start
                        if leftChild < len(queue) and queue[leftChild][0] < queue[smallest][0]:
                            smallest = leftChild
                        if rightChild < len(queue) and queue[rightChild][0] < queue[smallest][0]:
                            smallest = rightChild
                        if smallest == start:
                            break
                        queue[start], queue[smallest] = queue[smallest], queue[start]
                        start = smallest
                return initial

            while priorityQueue:
                currentDistance, currentVertex = popHeap(priorityQueue)
                if currentDistance > distances[currentVertex]:
                    continue
                for neighborVertex, edgeWeight in adjacencyMap[currentVertex]:
                    newDistance = currentDistance + edgeWeight
                    if newDistance < distances[neighborVertex]:
                        distances[neighborVertex] = newDistance
                        pushHeap(priorityQueue, (newDistance, neighborVertex))
            return distances[n - 1]

        outputList = []
        queryIndex = 0
        while True:
            if queryIndex > len(queries) - 1:
                break
            currentQuery = queries[queryIndex]
            sourceNode = currentQuery[0]
            destinationNode = currentQuery[1]
            adjacencyMap[sourceNode].append((destinationNode, 1))
            outputList.append(dijkstra())
            queryIndex += 1

        return outputList