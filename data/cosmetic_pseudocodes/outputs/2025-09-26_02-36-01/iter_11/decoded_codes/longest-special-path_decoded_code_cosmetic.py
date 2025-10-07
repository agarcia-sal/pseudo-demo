class Solution:
    def longestSpecialPath(self, edges, nums):
        n = len(nums)
        adjacency = [[] for _ in range(n)]

        def addToAdjacency(x, y, z):
            adjacency[x].append((y, z))

        def insertEdge(a, b, c):
            addToAdjacency(a, b, c)
            addToAdjacency(b, a, c)

        for uNode, vNode, edgeWeight in edges:
            insertEdge(uNode, vNode, edgeWeight)

        outerMax = 0
        outerMin = 1
        prefix = [0]
        lastSeenDepth = {}

        def dfs(current, predecessor, leftBound, depthCount):
            nonlocal outerMax, outerMin
            prevDepthVal = lastSeenDepth.get(nums[current], 0)
            lastSeenDepth[nums[current]] = depthCount
            if leftBound < prevDepthVal:
                leftBound = prevDepthVal

            segmentLen = prefix[-1] - prefix[leftBound]
            nodeCount = depthCount - leftBound

            if segmentLen > outerMax or (segmentLen == outerMax and nodeCount < outerMin):
                outerMax = segmentLen
                outerMin = nodeCount

            for i in range(len(adjacency[current])):
                vNeighbor, wWeight = adjacency[current][i]
                if vNeighbor != predecessor:
                    prefix.append(prefix[-1] + wWeight)
                    dfs(vNeighbor, current, leftBound, depthCount + 1)
                    prefix.pop()

            lastSeenDepth[nums[current]] = prevDepthVal

        dfs(0, -1, 0, 1)

        return [outerMax, outerMin]