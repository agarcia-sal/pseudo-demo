from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]

        def insertEdge(origin: int, destination: int, weight: int) -> None:
            graph[origin].append((destination, weight))

        def buildGraph(index: int) -> None:
            if index == len(edges):
                return
            startNode, endNode, edgeWeight = edges[index]
            insertEdge(startNode, endNode, edgeWeight)
            insertEdge(endNode, startNode, edgeWeight)
            buildGraph(index + 1)

        buildGraph(0)

        maxPathLength = 0
        minNodeCount = 1
        prefixSums = [0]
        nodeDepths = dict()  # key: nums value, value: depth count

        def dfs(current: int, previous: int, leftBound: int, depthCount: int) -> None:
            nonlocal maxPathLength, minNodeCount

            depthBefore = nodeDepths.get(nums[current], 0)
            nodeDepths[nums[current]] = depthCount
            if leftBound < depthBefore:
                leftBound = depthBefore

            currentLen = prefixSums[-1] - prefixSums[leftBound]
            nodeSpan = depthCount - leftBound

            if currentLen > maxPathLength:
                maxPathLength = currentLen
                minNodeCount = nodeSpan
            elif currentLen == maxPathLength and nodeSpan < minNodeCount:
                minNodeCount = nodeSpan

            edgeList = graph[current]
            def loop_nodes(edgeList: List[Tuple[int, int]], idx: int) -> None:
                if idx == len(edgeList):
                    return
                nbr, wght = edgeList[idx]
                if nbr != previous:
                    prefixSums.append(prefixSums[-1] + wght)
                    dfs(nbr, current, leftBound, depthCount + 1)
                    prefixSums.pop()
                loop_nodes(edgeList, idx + 1)

            loop_nodes(edgeList, 0)

            if depthBefore == 0:
                nodeDepths.pop(nums[current], None)
            else:
                nodeDepths[nums[current]] = depthBefore

        dfs(0, -1, 0, 1)
        return [maxPathLength, minNodeCount]