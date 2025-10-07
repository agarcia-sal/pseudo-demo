from math import inf
from collections import deque
from typing import List, Tuple

class Solution:

    def bfs(self, graph: List[List[int]], start: int) -> Tuple[int, int]:
        def dequeueAll(currQueue: deque, accFarthest: int, accMax: int):
            if not currQueue:
                return accFarthest, accMax
            else:
                xNode, yDist = currQueue.popleft()
                nextMax = accMax
                nextFarthest = accFarthest
                if yDist > accMax:
                    nextMax = yDist
                    nextFarthest = xNode

                def processNeighbors(neighList: List[int], visSet: List[bool], q: deque, idx: int):
                    if idx == len(neighList):
                        return visSet, q
                    else:
                        nb = neighList[idx]
                        if not visSet[nb]:
                            visSet[nb] = True
                            q.append((nb, yDist + 1))
                        return processNeighbors(neighList, visSet, q, idx + 1)

                visitedAfter, queueAfter = processNeighbors(graph[xNode], visited, currQueue, 0)
                return dequeueAll(queueAfter, nextFarthest, nextMax)

        lengthG = len(graph)
        visited = [False] * lengthG
        queue = deque()
        queue.append((start, 0))
        visited[start] = True
        farthestNode, maxDistance = dequeueAll(queue, start, 0)
        return farthestNode, maxDistance

    def tree_diameter(self, graph: List[List[int]]) -> int:
        zeroVal = 0
        startNode = zeroVal + 0
        tempA, _ = self.bfs(graph, startNode)
        _, diam = self.bfs(graph, tempA)
        return diam

    def maximum_path_length_from_node(self, graph: List[List[int]], node: int) -> int:
        def procQueue(qry: deque, visArr: List[bool], currMax: int) -> int:
            if not qry:
                return currMax
            else:
                pr = qry.popleft()
                qx_node, qy_dist = pr
                nxMax = currMax
                if qy_dist > currMax:
                    nxMax = qy_dist

                def innerNeigh(nlist: List[int], vSet: List[bool], queueLocal: deque, ind: int):
                    if ind == len(nlist):
                        return vSet, queueLocal
                    else:
                        xyN = nlist[ind]
                        if not vSet[xyN]:
                            vSet[xyN] = True
                            queueLocal.append((xyN, qy_dist + 1))
                        return innerNeigh(nlist, vSet, queueLocal, ind + 1)

                visUpdated, queueUpdated = innerNeigh(graph[qx_node], visArr, qry, 0)
                return procQueue(queueUpdated, visUpdated, nxMax)

        lenGraph = len(graph)
        visList = [False] * lenGraph
        qStore = deque()
        qStore.append((node, 0))
        visList[node] = True
        maxLen = procQueue(qStore, visList, 0)
        return maxLen

    def minimumDiameterAfterMerge(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> int:
        szN = len(edges1) + 1
        szM = len(edges2) + 1

        gph1 = [[] for _ in range(szN)]
        gph2 = [[] for _ in range(szM)]

        def buildGraph(edgList: List[Tuple[int, int]], gph: List[List[int]]):
            def loopEdges(idx: int):
                if idx >= len(edgList):
                    return
                else:
                    eU, eV = edgList[idx]
                    gph[eU].append(eV)
                    gph[eV].append(eU)
                    loopEdges(idx + 1)
            loopEdges(0)

        buildGraph(edges1, gph1)
        buildGraph(edges2, gph2)

        dia1 = self.tree_diameter(gph1)
        dia2 = self.tree_diameter(gph2)

        longestPath1 = [self.maximum_path_length_from_node(gph1, idx1) for idx1 in range(szN)]
        longestPath2 = [self.maximum_path_length_from_node(gph2, idx2) for idx2 in range(szM)]

        minDia = inf

        def checkAll(uIdx: int):
            nonlocal minDia
            if uIdx >= szN:
                return
            def checkInner(vIdx: int):
                nonlocal minDia
                if vIdx >= szM:
                    return
                candDia = dia1
                if dia2 > candDia:
                    candDia = dia2
                sumVal = longestPath1[uIdx] + longestPath2[vIdx] + 1
                if sumVal > candDia:
                    candDia = sumVal
                if candDia < minDia:
                    minDia = candDia
                checkInner(vIdx + 1)
            checkInner(0)
            checkAll(uIdx + 1)

        checkAll(0)
        return minDia