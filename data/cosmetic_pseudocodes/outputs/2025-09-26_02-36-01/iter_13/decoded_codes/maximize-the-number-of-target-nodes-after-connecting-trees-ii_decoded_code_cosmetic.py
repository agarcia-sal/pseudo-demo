from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        adjacencyMapOne = defaultdict(list)
        adjacencyMapTwo = defaultdict(list)

        def insertEdges(edgeList: List[Tuple[int, int]], adjacencyMap: defaultdict):
            for edge in edgeList:
                firstNode, secondNode = edge
                # Ensure both nodes exist in the adjacency map
                if firstNode not in adjacencyMap:
                    adjacencyMap[firstNode] = []
                if secondNode not in adjacencyMap:
                    adjacencyMap[secondNode] = []
                # Add edges bidirectionally
                adjacencyMap[firstNode].append(secondNode)
                adjacencyMap[secondNode].append(firstNode)

        insertEdges(edges1, adjacencyMapOne)
        insertEdges(edges2, adjacencyMapTwo)

        # total nodes based on keys; nodes might not be contiguous
        totalNodesOne = len(adjacencyMapOne)
        totalNodesTwo = len(adjacencyMapTwo)

        # To map node indices from 0 to totalNodes-1 for consistent BFS indexing,
        # we must map the keys to indices. The original pseudocode implicitly assumes contiguous indices from 0.
        # We create a mapping for nodes in each adjacency map.

        # Mapping for graph one
        sorted_nodes_one = sorted(adjacencyMapOne.keys())
        node_to_index_one = {node: idx for idx, node in enumerate(sorted_nodes_one)}
        index_to_node_one = {idx: node for idx, node in enumerate(sorted_nodes_one)}

        # Mapping for graph two
        sorted_nodes_two = sorted(adjacencyMapTwo.keys())
        node_to_index_two = {node: idx for idx, node in enumerate(sorted_nodes_two)}
        index_to_node_two = {idx: node for idx, node in enumerate(sorted_nodes_two)}

        # Rebuild adjacency maps with indices instead of original nodes for BFS
        adj_one = [[] for _ in range(totalNodesOne)]
        for node, neighbors in adjacencyMapOne.items():
            node_idx = node_to_index_one[node]
            for neigh in neighbors:
                neigh_idx = node_to_index_one[neigh]
                adj_one[node_idx].append(neigh_idx)

        adj_two = [[] for _ in range(totalNodesTwo)]
        for node, neighbors in adjacencyMapTwo.items():
            node_idx = node_to_index_two[node]
            for neigh in neighbors:
                neigh_idx = node_to_index_two[neigh]
                adj_two[node_idx].append(neigh_idx)

        def breadthFirstSearch(graph: List[List[int]], initial: int) -> Tuple[int, int]:
            countEven = 0
            countOdd = 0
            processingQueue = deque([(initial, 0)])
            markedVisited = {initial}

            while processingQueue:
                currentNode, currentDistance = processingQueue.popleft()
                if currentDistance % 2 == 0:
                    countEven += 1
                else:
                    countOdd += 1
                neighborsList = graph[currentNode]
                for potentialNeighbor in neighborsList:
                    if potentialNeighbor not in markedVisited:
                        markedVisited.add(potentialNeighbor)
                        processingQueue.append((potentialNeighbor, currentDistance + 1))
            return countEven, countOdd

        def gatherCounts(nodeCount: int, adjMap: List[List[int]]) -> List[Tuple[int, int]]:
            outputList = []
            def recurseGather(currentIndex: int):
                if currentIndex >= nodeCount:
                    return
                countsPair = breadthFirstSearch(adjMap, currentIndex)
                outputList.append(countsPair)
                recurseGather(currentIndex + 1)

            recurseGather(0)
            return outputList

        countsOne = gatherCounts(totalNodesOne, adj_one)
        countsTwo = gatherCounts(totalNodesTwo, adj_two)

        finalResultList = []

        def computeResult(indexOne: int):
            if indexOne >= totalNodesOne:
                return
            evenCountOne, oddCountOne = countsOne[indexOne]
            highestTargets = 0

            def scanIndexTwo(indexTwo: int):
                nonlocal highestTargets
                if indexTwo >= totalNodesTwo:
                    return
                evenCountTwo, oddCountTwo = countsTwo[indexTwo]
                # The pseudocode condition:
                # if indexOne == indexTwo or parity matches, targetCount = evenCountTwo else oddCountTwo
                if (indexOne == indexTwo) or ((indexOne % 2) == (indexTwo % 2)):
                    targetCount = evenCountTwo
                else:
                    targetCount = oddCountTwo
                if targetCount > highestTargets:
                    highestTargets = targetCount
                scanIndexTwo(indexTwo + 1)

            scanIndexTwo(0)
            finalResultList.append(evenCountOne + highestTargets)
            computeResult(indexOne + 1)

        computeResult(0)

        return finalResultList