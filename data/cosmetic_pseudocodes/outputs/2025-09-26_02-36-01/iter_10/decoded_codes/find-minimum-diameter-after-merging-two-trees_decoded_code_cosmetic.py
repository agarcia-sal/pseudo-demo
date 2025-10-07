from math import inf
from typing import List, Tuple

class Solution:
    def bfs(self, graph: List[List[int]], start: int) -> Tuple[int, int]:
        lenGraph = len(graph)
        marks = [False] * lenGraph
        deck = [(start, 0)]
        marks[start] = True
        furthestVertex = start
        maxDist = 0

        def deque_pop_left(aDeque: List[Tuple[int, int]]) -> Tuple[int, int]:
            ele = aDeque[0]
            del aDeque[0]
            return ele

        def enqueue(aDeque: List[Tuple[int, int]], val: Tuple[int, int]) -> None:
            aDeque.append(val)

        def recursive_iterate():
            nonlocal maxDist, furthestVertex
            if len(deck) == 0:
                return
            currTuple = deque_pop_left(deck)
            currentNode, distVal = currTuple
            if distVal > maxDist:
                maxDist = distVal
                furthestVertex = currentNode
            neighborsList = graph[currentNode]

            def process_neighbors(index: int):
                if index >= len(neighborsList):
                    return
                neigh = neighborsList[index]
                if not marks[neigh]:
                    marks[neigh] = True
                    enqueue(deck, (neigh, distVal + 1))
                process_neighbors(index + 1)

            process_neighbors(0)
            recursive_iterate()

        recursive_iterate()
        return furthestVertex, maxDist

    def tree_diameter(self, graph: List[List[int]]) -> int:
        zeroNode = 0
        nodeFarthest, _ = self.bfs(graph, zeroNode)
        _, diameterVal = self.bfs(graph, nodeFarthest)
        return diameterVal

    def maximum_path_length_from_node(self, graph: List[List[int]], node: int) -> int:
        sizeG = len(graph)
        visitMask = [False] * sizeG
        dq = [(node, 0)]
        visitMask[node] = True
        maxDistVal = 0

        def pop_left(dq_list: List[Tuple[int, int]]) -> Tuple[int, int]:
            itm = dq_list[0]
            del dq_list[0]
            return itm

        def queue_append(dq_list: List[Tuple[int, int]], val: Tuple[int, int]) -> None:
            dq_list.append(val)

        def recur_loop():
            nonlocal maxDistVal
            if len(dq) == 0:
                return
            tup = pop_left(dq)
            currentPoint, distNow = tup
            if distNow > maxDistVal:
                maxDistVal = distNow
            neighs = graph[currentPoint]

            def process_neighs(i: int):
                if i == len(neighs):
                    return
                nNode = neighs[i]
                if not visitMask[nNode]:
                    visitMask[nNode] = True
                    queue_append(dq, (nNode, distNow + 1))
                process_neighs(i + 1)

            process_neighs(0)
            recur_loop()

        recur_loop()
        return maxDistVal

    def minimumDiameterAfterMerge(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> int:
        sizeE1 = len(edges1) + 1
        sizeE2 = len(edges2) + 1

        G1 = [[] for _ in range(sizeE1)]
        G2 = [[] for _ in range(sizeE2)]

        def fill_graph(edges: List[Tuple[int, int]], graph: List[List[int]]) -> None:
            def recurse_i(j: int):
                if j == len(edges):
                    return
                x, y = edges[j]
                graph[x].append(y)
                graph[y].append(x)
                recurse_i(j + 1)
            recurse_i(0)

        fill_graph(edges1, G1)
        fill_graph(edges2, G2)

        diaOne = self.tree_diameter(G1)
        diaTwo = self.tree_diameter(G2)

        longestPaths1 = []
        idx1 = 0

        def gather_lp1():
            nonlocal idx1
            if idx1 == sizeE1:
                return
            longestPaths1.append(self.maximum_path_length_from_node(G1, idx1))
            idx1 += 1
            gather_lp1()

        gather_lp1()

        longestPaths2 = []
        idx2 = 0

        def gather_lp2():
            nonlocal idx2
            if idx2 == sizeE2:
                return
            longestPaths2.append(self.maximum_path_length_from_node(G2, idx2))
            idx2 += 1
            gather_lp2()

        gather_lp2()

        minDiam = inf
        uCtr = 0

        def outer_loop():
            nonlocal uCtr, minDiam
            if uCtr == sizeE1:
                return

            vCtr = 0

            def inner_loop():
                nonlocal vCtr, minDiam
                if vCtr == sizeE2:
                    return
                val1 = diaOne
                val2 = diaTwo
                val3 = longestPaths1[uCtr]
                val4 = longestPaths2[vCtr]
                candidate = val1
                if val2 > candidate:
                    candidate = val2
                if val3 + val4 + 1 > candidate:
                    candidate = val3 + val4 + 1
                if candidate < minDiam:
                    minDiam = candidate
                vCtr += 1
                inner_loop()

            inner_loop()
            uCtr += 1
            outer_loop()

        outer_loop()

        return minDiam