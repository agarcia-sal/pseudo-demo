from typing import List

class UnionFind:
    def __init__(self, count: int):
        self.parent = [i for i in range(count)]
        self.height = [0] * count

    def find(self, node: int) -> int:
        def innerFind(n: int) -> int:
            if self.parent[n] == n:
                return n
            holder = innerFind(self.parent[n])
            self.parent[n] = holder
            return holder
        return innerFind(node)

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.height[rootX] > self.height[rootY]:
                self.parent[rootY] = rootX
            else:
                if self.height[rootY] > self.height[rootX]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.height[rootX] += 1

class Solution:
    def maximizeSumOfWeights(self, edgeList: List[List[int]], maxDegree: int) -> int:
        totalNodes = len(edgeList) + 1
        degList = [0] * totalNodes
        disjointSet = UnionFind(totalNodes)

        def descendingComparator(a: List[int], b: List[int]) -> int:
            if a[2] > b[2]:
                return -1
            elif a[2] < b[2]:
                return 1
            else:
                return 0

        def sortDescending(arr: List[List[int]]) -> None:
            def swapElements(i: int, j: int) -> None:
                arr[i], arr[j] = arr[j], arr[i]

            def quickSortLowHigh(low: int, high: int) -> None:
                if low >= high:
                    return
                pivotIndex = low
                leftIndex = low + 1
                rightIndex = high

                while leftIndex <= rightIndex:
                    while leftIndex <= high and descendingComparator(arr[leftIndex], arr[pivotIndex]) < 0:
                        leftIndex += 1
                    while rightIndex >= low and descendingComparator(arr[rightIndex], arr[pivotIndex]) > 0:
                        rightIndex -= 1
                    if leftIndex <= rightIndex:
                        swapElements(leftIndex, rightIndex)
                        leftIndex += 1
                        rightIndex -= 1

                swapElements(pivotIndex, rightIndex)
                quickSortLowHigh(low, rightIndex - 1)
                quickSortLowHigh(rightIndex + 1, high)

            quickSortLowHigh(0, len(arr) - 1)

        sortDescending(edgeList)

        accumulator = 0
        indexer = 0
        totalEdges = len(edgeList)
        while indexer < totalEdges:
            currentEdge = edgeList[indexer]
            firstNode, secondNode, weightVal = currentEdge

            if not (degList[firstNode] >= maxDegree or degList[secondNode] >= maxDegree) and disjointSet.find(firstNode) != disjointSet.find(secondNode):
                disjointSet.union(firstNode, secondNode)
                degList[firstNode] += 1
                degList[secondNode] += 1
                accumulator += weightVal

            indexer += 1

        return accumulator