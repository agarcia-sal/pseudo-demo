from typing import List, Dict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        container = [[] for _ in range(len(nums))]

        def addEdgePairs(nodeA: int, nodeB: int, weightValue: int) -> None:
            container[nodeA].append([nodeB, weightValue])
            container[nodeB].append([nodeA, weightValue])

        for edgeElem in edges:
            firstNode, secondNode, weightVal = edgeElem
            addEdgePairs(firstNode, secondNode, weightVal)

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth: Dict[int, int] = {}

        def dfs(currNode: int, prevNode: int, boundaryLeft: int, depthCount: int) -> None:
            nonlocal maxLength, minNodes

            previousDepth = 0
            if nums[currNode] in lastSeenDepth:
                previousDepth = lastSeenDepth[nums[currNode]]

            lastSeenDepth[nums[currNode]] = depthCount

            if boundaryLeft < previousDepth:
                boundaryLeft = previousDepth

            lenDiff = prefix[-1] - prefix[boundaryLeft]
            numNodes = depthCount - boundaryLeft

            if (lenDiff > maxLength) or (lenDiff == maxLength and numNodes < minNodes):
                maxLength = lenDiff
                minNodes = numNodes

            for nextNode, wgt in container[currNode]:
                if nextNode == prevNode:
                    continue
                prefix.append(prefix[-1] + wgt)
                dfs(nextNode, currNode, boundaryLeft, depthCount + 1)
                prefix.pop()

            lastSeenDepth[nums[currNode]] = previousDepth

        dfs(0, -1, 0, 1)

        return [maxLength, minNodes]