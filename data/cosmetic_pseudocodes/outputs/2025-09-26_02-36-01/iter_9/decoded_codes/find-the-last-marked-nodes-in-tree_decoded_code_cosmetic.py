class Solution:
    def lastMarkedNodes(self, edges):
        def explore(node, parent, distances):
            for neighbor in g[node]:
                if neighbor != parent:
                    distances[neighbor] = distances[node] + 1
                    explore(neighbor, node, distances)

        totalNodes = len(edges) + 1
        g = [[] for _ in range(totalNodes)]

        for uNode, vNode in edges:
            g[uNode].append(vNode)
            g[vNode].append(uNode)

        distFirst = [-1] * totalNodes
        distFirst[0] = 0
        explore(0, -1, distFirst)

        farNodeA = 0
        maxDistA = distFirst[0]
        for idxA in range(totalNodes):
            if distFirst[idxA] > maxDistA:
                farNodeA = idxA
                maxDistA = distFirst[idxA]

        distSecond = [-1] * totalNodes
        distSecond[farNodeA] = 0
        explore(farNodeA, -1, distSecond)

        farNodeB = 0
        maxDistB = distSecond[0]
        for idxB in range(totalNodes):
            if distSecond[idxB] > maxDistB:
                farNodeB = idxB
                maxDistB = distSecond[idxB]

        distThird = [-1] * totalNodes
        distThird[farNodeB] = 0
        explore(farNodeB, -1, distThird)

        res = []
        for pos in range(totalNodes):
            valX = distSecond[pos]
            valY = distThird[pos]
            if valX <= valY:
                res.append(farNodeB)
            else:
                res.append(farNodeA)

        return res