from collections import defaultdict

class Solution:
    def longestSpecialPath(self, edges, nums):
        n = len(nums)
        adjList = [[] for _ in range(n)]

        def buildAdjacency():
            for a, b, cost in edges:
                adjList[a].append((b, cost))
                adjList[b].append((a, cost))

        buildAdjacency()

        maximumLength = 0
        minimumNodes = 1
        cumulativeCosts = [0]
        depthRecord = dict()

        def explore(node, parentNode, leftLim, depthCount):
            nonlocal maximumLength, minimumNodes
            prevDepth = depthRecord.get(nums[node], 0)
            depthRecord[nums[node]] = depthCount

            if leftLim < prevDepth:
                leftLim = prevDepth

            pathLength = cumulativeCosts[-1] - cumulativeCosts[leftLim]
            nodeSpan = depthCount - leftLim

            if pathLength > maximumLength or (pathLength == maximumLength and nodeSpan < minimumNodes):
                maximumLength = pathLength
                minimumNodes = nodeSpan

            for neighbor, weight in adjList[node]:
                if neighbor == parentNode:
                    continue
                newCost = cumulativeCosts[-1] + weight
                cumulativeCosts.append(newCost)
                explore(neighbor, node, leftLim, depthCount + 1)
                cumulativeCosts.pop()

            depthRecord[nums[node]] = prevDepth

        explore(0, -1, 0, 1)
        return [maximumLength, minimumNodes]