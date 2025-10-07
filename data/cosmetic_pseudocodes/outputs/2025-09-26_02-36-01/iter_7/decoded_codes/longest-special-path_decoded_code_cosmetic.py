from typing import List, Dict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        def get_initial_graph() -> List[List[List[int]]]:
            return [[] for _ in range(len(nums))]

        connectivityMap = get_initial_graph()

        for edge in edges:
            fromNode, toNode, distanceVal = edge
            connectivityMap[fromNode].append([toNode, distanceVal])
            connectivityMap[toNode].append([fromNode, distanceVal])

        maximumPathLength = 0
        smallestNodeCount = 1
        accumulatedWeights = [0]
        depthsObserved: Dict[int, int] = {}

        def explore(current: int, last: int, leftBoundaryIndex: int, currentDepthCount: int) -> None:
            nonlocal maximumPathLength, smallestNodeCount

            previousDepthVal = depthsObserved.get(nums[current], 0)
            depthsObserved[nums[current]] = currentDepthCount

            if leftBoundaryIndex < previousDepthVal:
                leftBoundaryIndex = previousDepthVal

            pathLengthCalc = accumulatedWeights[-1] - accumulatedWeights[leftBoundaryIndex]
            nodeSpanCalc = currentDepthCount - leftBoundaryIndex

            if (pathLengthCalc > maximumPathLength) or (pathLengthCalc == maximumPathLength and nodeSpanCalc < smallestNodeCount):
                maximumPathLength = pathLengthCalc
                smallestNodeCount = nodeSpanCalc

            def recurse_over(adjacents: List[List[int]], idx: int) -> None:
                if idx >= len(adjacents):
                    return
                neighborNode, edgeWeight = adjacents[idx]

                if neighborNode != last:
                    accumulatedWeights.append(accumulatedWeights[-1] + edgeWeight)
                    explore(neighborNode, current, leftBoundaryIndex, currentDepthCount + 1)
                    accumulatedWeights.pop()

                recurse_over(adjacents, idx + 1)

            recurse_over(connectivityMap[current], 0)
            depthsObserved[nums[current]] = previousDepthVal

        explore(0, -1, 0, 1)

        return [maximumPathLength, smallestNodeCount]