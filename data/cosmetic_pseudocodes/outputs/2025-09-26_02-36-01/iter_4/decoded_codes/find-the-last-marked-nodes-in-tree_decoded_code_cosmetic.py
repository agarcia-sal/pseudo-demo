class Solution:
    def lastMarkedNodes(self, edges):
        def dfs(currentNode, parentNode, distanceList):
            for neighbor in g[currentNode]:
                if neighbor != parentNode:
                    distanceList[neighbor] = distanceList[currentNode] + 1
                    dfs(neighbor, currentNode, distanceList)

        totalNodes = len(edges) + 1
        g = [[] for _ in range(totalNodes)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        dist1 = [-1] * totalNodes
        dist1[0] = 0
        dfs(0, -1, dist1)

        maxDistance1 = dist1[0]
        a = 0
        for i in range(totalNodes):
            if dist1[i] > maxDistance1:
                maxDistance1 = dist1[i]
                a = i

        dist2 = [-1] * totalNodes
        dist2[a] = 0
        dfs(a, -1, dist2)

        maxDistance2 = dist2[0]
        b = 0
        for i in range(totalNodes):
            if dist2[i] > maxDistance2:
                maxDistance2 = dist2[i]
                b = i

        dist3 = [-1] * totalNodes
        dist3[b] = 0
        dfs(b, -1, dist3)

        result = []
        for i in range(totalNodes):
            if dist2[i] > dist3[i]:
                result.append(a)
            else:
                result.append(b)
        return result