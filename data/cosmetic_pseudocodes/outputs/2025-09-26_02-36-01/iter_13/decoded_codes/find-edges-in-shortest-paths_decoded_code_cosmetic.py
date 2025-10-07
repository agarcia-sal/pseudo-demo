class Solution:
    def findAnswer(self, n, edges):
        def heapPop(h):
            if len(h) == 0:
                return None
            i, x = 0, h[0]
            last = h.pop()
            if len(h) > 0:
                h[0] = last
                while True:
                    left = 2 * i + 1
                    right = 2 * i + 2
                    smallest = i
                    if left < len(h) and h[left][0] < h[smallest][0]:
                        smallest = left
                    if right < len(h) and h[right][0] < h[smallest][0]:
                        smallest = right
                    if smallest == i:
                        break
                    h[i], h[smallest] = h[smallest], h[i]
                    i = smallest
            return x

        def heapPush(h, val):
            h.append(val)
            i = len(h) - 1
            while i > 0:
                parent = (i - 1) // 2
                if h[parent][0] <= h[i][0]:
                    break
                h[i], h[parent] = h[parent], h[i]
                i = parent

        def _min(a, b):
            return a if a < b else b

        def _max(a, b):
            return a if a > b else b

        adjacencyMap = {}
        indexCounter = 0

        def edgeIterator():
            nonlocal indexCounter
            if indexCounter >= len(edges):
                return None
            e = edges[indexCounter]
            indexCounter += 1
            return e

        while True:
            edgeTriplet = edgeIterator()
            if edgeTriplet is None:
                break
            fromNode, toNode, edgeWeight = edgeTriplet
            if fromNode not in adjacencyMap:
                adjacencyMap[fromNode] = []
            if toNode not in adjacencyMap:
                adjacencyMap[toNode] = []
            adjacencyMap[fromNode].append([toNode, edgeWeight])
            adjacencyMap[toNode].append([fromNode, edgeWeight])

        INF = float('inf')
        distances = []
        distBuildIndex = 0
        while distBuildIndex < n:
            distances.append(INF)
            distBuildIndex += 1

        distances[0] = 0
        priorityQueue = []
        heapPush(priorityQueue, [0, 0])

        def recurseWhileNonEmptyPq(queue):
            if len(queue) == 0:
                return
            pair = heapPop(queue)
            if pair is None:
                return
            cd, u = pair
            if cd > distances[u]:
                recurseWhileNonEmptyPq(queue)
            else:
                neighbors = adjacencyMap.get(u, None)
                if neighbors is not None:
                    ni = 0
                    while ni < len(neighbors):
                        v, w = neighbors[ni]
                        candidate = cd + w
                        if candidate < distances[v]:
                            distances[v] = candidate
                            heapPush(queue, [candidate, v])
                        ni += 1
                recurseWhileNonEmptyPq(queue)

        recurseWhileNonEmptyPq(priorityQueue)

        shortestPathEdges = set()
        dfsStack = []
        dfsStack.append([n - 1, distances[n - 1]])
        visitedFlags = []
        vfIndex = 0
        while vfIndex < n:
            visitedFlags.append(False)
            vfIndex += 1

        def dfsProcess():
            if len(dfsStack) == 0:
                return
            currentPair = dfsStack.pop()
            u = currentPair[0]
            distU = currentPair[1]
            if visitedFlags[u]:
                dfsProcess()
                return
            visitedFlags[u] = True
            adjacents = adjacencyMap.get(u, None)
            iteratorIndex = 0
            while adjacents is not None and iteratorIndex < len(adjacents):
                v, w = adjacents[iteratorIndex]
                if distU == distances[v] + w:
                    x = _min(u, v)
                    y = _max(u, v)
                    shortestPathEdges.add((x, y))  # tuples for set
                    dfsStack.append([v, distances[v]])
                iteratorIndex += 1
            dfsProcess()

        dfsProcess()

        resultList = []
        edgeInd = 0
        while edgeInd < len(edges):
            u, v, _ = edges[edgeInd]
            lesserNode = _min(u, v)
            greaterNode = _max(u, v)
            contained = (lesserNode, greaterNode) in shortestPathEdges
            resultList.append(contained)
            edgeInd += 1

        return resultList