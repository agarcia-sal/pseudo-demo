from typing import List, Dict, Tuple


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # Build an empty adjacency list with length = len(nums)
        def recursionBuildGraph(index: int, limit: int, accumulator: List[List[Tuple[int, int]]]) -> List[List[Tuple[int, int]]]:
            if index >= limit:
                return accumulator
            return recursionBuildGraph(index + 1, limit, accumulator + [[]])

        graph: List[List[Tuple[int, int]]] = recursionBuildGraph(0, len(nums), [])

        def appendEdge(sourceIdx: int, targetIdx: int, wgt: int, gph: List[List[Tuple[int, int]]]) -> None:
            edgeTuple = (targetIdx, wgt)
            currentAdjacency = gph[sourceIdx]
            # Using list concatenation as in pseudocode guarantees a new list creation
            gph[sourceIdx] = currentAdjacency + [edgeTuple]

        for edgeTriple in edges:
            startVertex, endVertex, weightValue = edgeTriple
            appendEdge(startVertex, endVertex, weightValue, graph)
            appendEdge(endVertex, startVertex, weightValue, graph)

        maxLen = 0
        minCount = 1
        prefixSum = [0]
        lastSeen: Dict[int, int] = {}
        arrNums = nums

        def myDfs(currentNode: int, previousNode: int, leftBound: int, depthLevel: int) -> None:
            nonlocal maxLen, minCount, prefixSum, lastSeen

            previousDepth = 0
            if arrNums[currentNode] in lastSeen:
                previousDepth = lastSeen[arrNums[currentNode]]
            lastSeen[arrNums[currentNode]] = depthLevel

            if leftBound < previousDepth:
                leftBound = previousDepth

            prefixLength = prefixSum[-1] - prefixSum[leftBound]
            nodeCount = depthLevel - leftBound

            if (prefixLength > maxLen) or (prefixLength == maxLen and nodeCount < minCount):
                maxLen = prefixLength
                minCount = nodeCount

            def dfsIterative(index: int, neighbors: List[Tuple[int, int]]) -> None:
                if index >= len(neighbors):
                    return
                nextNode, weightVal = neighbors[index]
                if nextNode != previousNode:
                    prefixSum.append(prefixSum[-1] + weightVal)
                    myDfs(nextNode, currentNode, leftBound, depthLevel + 1)
                    prefixSum.pop()
                dfsIterative(index + 1, neighbors)

            dfsIterative(0, graph[currentNode])
            lastSeen[arrNums[currentNode]] = previousDepth

        myDfs(0, -1, 0, 1)
        return [maxLen, minCount]