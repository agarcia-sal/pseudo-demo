from math import inf

class Solution:
    def bfs(self, graph, start):
        lenGraph = len(graph)
        flagArray = [False] * lenGraph
        queueDeq = [(start, 0)]
        flagArray[start] = True
        farNode = start
        maxDist = 0

        while queueDeq:
            currentNode, currentDistance = queueDeq.pop(0)

            if currentDistance > maxDist:
                maxDist = currentDistance
                farNode = currentNode

            neighborsList = graph[currentNode]
            for nb in neighborsList:
                if not flagArray[nb]:
                    flagArray[nb] = True
                    queueDeq.append((nb, currentDistance + 1))

        return farNode, maxDist

    def tree_diameter(self, graph):
        initialNode = 0
        tempNode, _ = self.bfs(graph, initialNode)
        _, maxDiameter = self.bfs(graph, tempNode)
        return maxDiameter

    def maximum_path_length_from_node(self, graph, node):
        totalNodes = len(graph)
        visitedMarks = [False] * totalNodes
        deqList = [(node, 0)]
        visitedMarks[node] = True
        distanceMax = 0

        while deqList:
            currNode, currDist = deqList.pop(0)

            if currDist > distanceMax:
                distanceMax = currDist

            nbrs = graph[currNode]
            for adj in nbrs:
                if not visitedMarks[adj]:
                    visitedMarks[adj] = True
                    deqList.append((adj, currDist + 1))

        return distanceMax

    def minimumDiameterAfterMerge(self, edges1, edges2):
        length1 = len(edges1)
        sizeN = length1 + 1
        length2 = len(edges2)
        sizeM = length2 + 1

        graphOne = [[] for _ in range(sizeN)]
        graphTwo = [[] for _ in range(sizeM)]

        for pairE in edges1:
            uN, vN = pairE
            graphOne[uN].append(vN)
            graphOne[vN].append(uN)

        for pairF in edges2:
            uM, vM = pairF
            graphTwo[uM].append(vM)
            graphTwo[vM].append(uM)

        diamOne = self.tree_diameter(graphOne)
        diamTwo = self.tree_diameter(graphTwo)

        longestPathOne = [self.maximum_path_length_from_node(graphOne, c1) for c1 in range(sizeN)]
        longestPathTwo = [self.maximum_path_length_from_node(graphTwo, c2) for c2 in range(sizeM)]

        minDiamVal = inf
        for posU in range(sizeN):
            for posV in range(sizeM):
                candidateDiam = longestPathOne[posU] + longestPathTwo[posV] + 1
                if diamOne > candidateDiam or diamTwo > candidateDiam:
                    candidateDiam = max(diamOne, diamTwo)
                if candidateDiam < minDiamVal:
                    minDiamVal = candidateDiam

        return minDiamVal