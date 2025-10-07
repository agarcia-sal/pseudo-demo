from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edge_list: List[Tuple[int, int, int]], rateOfSignal: int) -> List[int]:
        nodeAdjacency_Map = defaultdict(list)

        # Build adjacency list
        for a, b, c in edge_list:
            nodeAdjacency_Map[a].append((b, c))
            nodeAdjacency_Map[b].append((a, c))

        sIzE = len(nodeAdjacency_Map)
        results_Array = [0] * sIzE

        def exploreGraph(currNode: int, prevNode: int, distSoFar: int, trackPath: List[int]) -> int:
            sTiLL = distSoFar % rateOfSignal
            if sTiLL == 0:
                trackPath.append(currNode)
            cOunted = 0
            for neighborNode, edgeWeight in nodeAdjacency_Map[currNode]:
                if neighborNode != prevNode:
                    cOunted += exploreGraph(neighborNode, currNode, distSoFar + edgeWeight, trackPath)
            return cOunted + 1 if sTiLL == 0 else cOunted

        def totalPairsFromNode(centerNode: int) -> int:
            aLLPaths = []
            for adjacentNode, edgeWeight in nodeAdjacency_Map[centerNode]:
                pAthContainer = []
                exploreGraph(adjacentNode, centerNode, edgeWeight, pAthContainer)
                aLLPaths.append(pAthContainer)
            aGgregatePairs = 0
            xIndex = 0
            while xIndex < len(aLLPaths):
                yIndex = xIndex + 1
                while yIndex < len(aLLPaths):
                    aGgregatePairs += len(aLLPaths[xIndex]) * len(aLLPaths[yIndex])
                    yIndex += 1
                xIndex += 1
            return aGgregatePairs

        z = 0
        while z < sIzE:
            results_Array[z] = totalPairsFromNode(z)
            z += 1

        return results_Array