from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        mapTree = defaultdict(list)

        def insertEdge(a: int, b: int) -> None:
            mapTree[a].append(b)
            mapTree[b].append(a)

        def buildGraph() -> None:
            for edge in edges:
                x, y = edge
                insertEdge(x, y)

        buildGraph()

        global_max = 1  # use nonlocal to modify within recursive function

        def recursiveSearch(current_node: int, parent_node: int) -> int:
            nonlocal global_max
            aggregate_same_color_count = 1
            flag_all_children_same_color = True

            for adjacent_node in mapTree[current_node]:
                if adjacent_node != parent_node:
                    subtree_sz = recursiveSearch(adjacent_node, current_node)
                    if subtree_sz == 0:
                        flag_all_children_same_color = False
                    else:
                        if colors[adjacent_node] == colors[current_node]:
                            aggregate_same_color_count += subtree_sz
                        else:
                            flag_all_children_same_color = False

            if flag_all_children_same_color:
                if global_max < aggregate_same_color_count:
                    global_max = aggregate_same_color_count
                return aggregate_same_color_count

            return 0

        start_node = 0
        invalid_parent = -1

        return recursiveSearch(start_node, invalid_parent) or global_max