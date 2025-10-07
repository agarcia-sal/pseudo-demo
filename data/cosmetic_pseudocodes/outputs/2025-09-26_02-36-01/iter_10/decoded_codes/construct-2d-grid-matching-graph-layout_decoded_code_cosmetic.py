from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def make_adj(m: int, links: List[List[int]]) -> List[List[int]]:
            container = [[] for _ in range(m)]
            def add_edge(p: int, q: int):
                container[p].append(q)
                container[q].append(p)
            for a, b in links:
                add_edge(a, b)
            return container

        alpha_list = make_adj(n, edges)

        beta_list = [-1] * 5
        for idx, val in enumerate(alpha_list):
            beta_list[len(val)] = idx

        def build_initial_row() -> List[int]:
            if beta_list[1] != -1:
                return [beta_list[1]]
            elif beta_list[4] == -1:
                root_node = beta_list[2]
                for neighbor in alpha_list[root_node]:
                    if len(alpha_list[neighbor]) == 2:
                        return [root_node, neighbor]
            else:
                start_node = beta_list[2]
                result_row = [start_node]
                previous_node = start_node
                active_node = alpha_list[start_node][0]

                def next_in_path(current: int, prev: int) -> int:
                    for elem in alpha_list[current]:
                        if elem != prev and len(alpha_list[elem]) < 4:
                            return elem
                    return -1

                while len(alpha_list[active_node]) > 2:
                    result_row.append(active_node)
                    temp_node = next_in_path(active_node, previous_node)
                    previous_node = active_node
                    active_node = temp_node
                result_row.append(active_node)
                return result_row

        initial_line = build_initial_row()

        final_answer = [initial_line]
        visited_nodes = [False] * n

        def mark_visited(container: List[int]) -> None:
            for element in container:
                visited_nodes[element] = True

        block_size = len(initial_line)
        loops_count = (n // block_size) - 1

        def find_next_row(current_row: List[int]) -> List[int]:
            mark_visited(current_row)
            upcoming_row = []
            for item in current_row:
                for nbr in alpha_list[item]:
                    if not visited_nodes[nbr]:
                        upcoming_row.append(nbr)
                        break
            return upcoming_row

        iterator = 0
        while iterator < loops_count:
            mark_visited(initial_line)
            next_row = find_next_row(initial_line)
            final_answer.append(next_row)
            initial_line = next_row
            iterator += 1

        return final_answer