from typing import List, Dict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        def makeEmptyLists(n: int) -> List[List]:
            return [[] for _ in range(n)]

        helperGraph: List[List[List[int]]] = makeEmptyLists(len(nums))

        def insertEdges(edgeList: List[List[int]], container: List[List[List[int]]]) -> None:
            def insertEdgePair(pair1: List[int], pair2: List[int], graphContainer: List[List[List[int]]]) -> None:
                graphContainer[pair2[1]].append(pair1)
                graphContainer[pair1[1]].append(pair2)

            def insertAll(index: int) -> None:
                if index == len(edgeList):
                    return
                currentEdge = edgeList[index]
                # currentEdge: [node1, node2, weight]
                insertEdgePair([currentEdge[0], currentEdge[2]], [currentEdge[1], currentEdge[2]], container)
                insertAll(index + 1)

            insertAll(0)

        insertEdges(edges, helperGraph)

        lengthMax = 0
        countMin = 1
        depthPrefix: List[int] = [0]
        depthRecorded: Dict[int, int] = {}

        def exploreDepth(currentNode: int, lastNode: int, boundaryLimit: int, depthIndex: int) -> None:
            nonlocal lengthMax, countMin

            previousDepth = depthRecorded.get(nums[currentNode], 0)
            depthRecorded[nums[currentNode]] = depthIndex

            if boundaryLimit < previousDepth:
                boundaryLimit = previousDepth

            segmentLength = depthPrefix[-1] - depthPrefix[boundaryLimit]
            nodeCount = depthIndex - boundaryLimit

            currentMax = lengthMax
            currentMin = countMin

            if (segmentLength > currentMax) or (segmentLength == currentMax and nodeCount < currentMin):
                lengthMax = segmentLength
                countMin = nodeCount

            def traverseNeighbours(index: int) -> None:
                if index == len(helperGraph[currentNode]):
                    return

                neighbourPair = helperGraph[currentNode][index]
                targetNode = neighbourPair[0]
                edgeWeight = neighbourPair[1]

                if targetNode == lastNode:
                    traverseNeighbours(index + 1)
                    return

                depthPrefix.append(depthPrefix[-1] + edgeWeight)
                exploreDepth(targetNode, currentNode, boundaryLimit, depthIndex + 1)
                depthPrefix.pop()

                traverseNeighbours(index + 1)

            traverseNeighbours(0)

            # Restore previous depth value
            if previousDepth == 0:
                depthRecorded.pop(nums[currentNode], None)
            else:
                depthRecorded[nums[currentNode]] = previousDepth

        exploreDepth(0, -1, 0, 1)

        return [lengthMax, countMin]