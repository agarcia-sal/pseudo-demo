from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        graph = defaultdict(list)

        def insert_edge(x: int, y: int) -> None:
            graph[x].append(y)
            graph[y].append(x)

        for a, b in edges:
            insert_edge(a, b)

        result = 1

        def depth_search(p: int, q: int) -> int:
            nonlocal result
            alpha = 1
            flag = True

            def iter_neighbors(index: int, listN: List[int]) -> None:
                nonlocal alpha, flag
                if index >= len(listN):
                    return
                neighbor_node = listN[index]
                if neighbor_node != q:
                    count_subtree = depth_search(neighbor_node, p)
                    if count_subtree == 0:
                        flag = False
                    else:
                        if colors[neighbor_node] == colors[p]:
                            alpha += count_subtree
                        else:
                            flag = False

                iter_neighbors(index + 1, listN)

            iter_neighbors(0, graph[p])
            if flag:
                if result < alpha:
                    result = alpha
                return alpha
            else:
                return 0

        return depth_search(0, -1)