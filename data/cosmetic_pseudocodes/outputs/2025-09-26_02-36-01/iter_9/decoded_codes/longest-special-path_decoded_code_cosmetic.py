from typing import List, Tuple, Dict

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        def buildGraph(edgeList: List[Tuple[int, int, int]], size: int) -> List[List[Tuple[int, int]]]:
            adjList = [[] for _ in range(size)]
            idx = 0
            while idx < len(edgeList):
                fromNode, toNode, weightVal = edgeList[idx]
                addEdge(adjList, fromNode, toNode, weightVal)
                addEdge(adjList, toNode, fromNode, weightVal)
                idx += 1
            return adjList

        def addEdge(graphStructure: List[List[Tuple[int, int]]], source: int, target: int, wgt: int) -> None:
            pushPair(graphStructure[source], target, wgt)

        def pushPair(listRef: List[Tuple[int, int]], vertexVal: int, weightVal: int) -> None:
            pairToAdd = (vertexVal, weightVal)
            listRef.append(pairToAdd)

        def appendPrefix(lst: List[int], val: int) -> None:
            lst.append(val)

        def popPrefix(lst: List[int]) -> None:
            lst.pop()

        def depthFirstSearch(current: int, previous: int, boundaryLeft: int, depthCount: int) -> None:
            nonlocal maxLength, minNodes
            prevDepthVal = 0
            curNum = nums[current]
            if curNum in lastSeenDepth:
                prevDepthVal = lastSeenDepth[curNum]
            lastSeenDepth[curNum] = depthCount

            if boundaryLeft < prevDepthVal:
                boundaryLeft = prevDepthVal

            segmentLength = prefix[-1] - prefix[boundaryLeft]
            segmentNodes = depthCount - boundaryLeft

            if segmentLength > maxLength or (segmentLength == maxLength and segmentNodes < minNodes):
                maxLength = segmentLength
                minNodes = segmentNodes

            for vert, wgt in graph[current]:
                if vert == previous:
                    continue
                appendPrefix(prefix, prefix[-1] + wgt)
                depthFirstSearch(vert, current, boundaryLeft, depthCount + 1)
                popPrefix(prefix)

            lastSeenDepth[curNum] = prevDepthVal

        graph = buildGraph(edges, len(nums))
        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth: Dict[int, int] = {}

        depthFirstSearch(0, -1, 0, 1)
        return [maxLength, minNodes]