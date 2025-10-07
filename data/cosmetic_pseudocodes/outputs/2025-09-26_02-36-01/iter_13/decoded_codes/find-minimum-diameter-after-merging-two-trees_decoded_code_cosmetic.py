class Solution:
    def bfs(self, graph, start):
        lengthGraph = len(graph)
        flags = [False] * lengthGraph

        q = []
        q.append((start, 0))
        flags[start] = True

        currentFarthest = start
        greatestDistance = 0

        while q:
            currentNode, currentDistance = q.pop(0)
            if currentDistance > greatestDistance:
                greatestDistance = currentDistance
                currentFarthest = currentNode

            for neighbor in graph[currentNode]:
                if not flags[neighbor]:
                    flags[neighbor] = True
                    q.append((neighbor, currentDistance + 1))

        return currentFarthest, greatestDistance

    def tree_diameter(self, graph):
        startNode = 0
        farNode, _ = self.bfs(graph, startNode)
        _, treeDiameter = self.bfs(graph, farNode)
        return treeDiameter

    def maximum_path_length_from_node(self, graph, node):
        lengthGraph = len(graph)
        flags = [False] * lengthGraph

        queue = [(node, 0)]
        flags[node] = True
        maxDist = 0

        while queue:
            currentNode, currentDist = queue.pop(0)
            if currentDist > maxDist:
                maxDist = currentDist
            for ng in graph[currentNode]:
                if not flags[ng]:
                    flags[ng] = True
                    queue.append((ng, currentDist + 1))
        return maxDist

    def minimumDiameterAfterMerge(self, edges1, edges2):
        len1 = len(edges1) + 1
        len2 = len(edges2) + 1

        def createEmptyLists(size, acc):
            if size == 0:
                return acc
            return createEmptyLists(size - 1, acc + [[]])

        graphOne = createEmptyLists(len1, [])
        graphTwo = createEmptyLists(len2, [])

        def buildGraph(edges, graph, idx):
            if idx >= len(edges):
                return graph
            u, v = edges[idx]
            graph[u].append(v)
            graph[v].append(u)
            return buildGraph(edges, graph, idx + 1)

        graphOne = buildGraph(edges1, graphOne, 0)
        graphTwo = buildGraph(edges2, graphTwo, 0)

        diam1 = self.tree_diameter(graphOne)
        diam2 = self.tree_diameter(graphTwo)

        def gatherLongestPaths(graph, size, acc, idx):
            if idx >= size:
                return acc
            maxPath = self.maximum_path_length_from_node(graph, idx)
            return gatherLongestPaths(graph, size, acc + [maxPath], idx + 1)

        longestPaths1 = gatherLongestPaths(graphOne, len1, [], 0)
        longestPaths2 = gatherLongestPaths(graphTwo, len2, [], 0)

        infinityVal = float('inf')
        minDiameterVal = infinityVal

        def maxVal(a, b):
            return a if a > b else b

        def compareLoopV(v, currentMin, u):
            if v >= len2:
                return currentMin
            candidate = longestPaths1[u] + longestPaths2[v] + 1
            newDiameter = maxVal(diam1, maxVal(diam2, candidate))
            nextMin = currentMin
            if newDiameter < currentMin:
                nextMin = newDiameter
            return compareLoopV(v + 1, nextMin, u)

        def compareLoopU(u):
            nonlocal minDiameterVal
            if u >= len1:
                return minDiameterVal
            bestForU = compareLoopV(0, minDiameterVal, u)
            if bestForU < minDiameterVal:
                minDiameterVal = bestForU
            return compareLoopU(u + 1)

        return compareLoopU(0)