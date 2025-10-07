from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:

        def substitute_modulo(a: int, b: int) -> int:
            return a - (a // b) * b

        def substitute_length(container) -> int:
            count = 0
            iter_var = container
            # container is indexable (list), so count length without using len()
            # but to preserve semantics, we just simulate the loop
            # since container is list, it's safe to use len(container) directly
            # but to respect pseudocode, implement loop counting
            for _ in iter_var:
                count += 1
            return count

        def push_to_list(lst: List, val) -> None:
            lst_length = substitute_length(lst)
            if lst_length == len(lst):
                lst.append(val)
            else:
                lst[lst_length] = val

        graph = defaultdict(list)
        idx_x = 0
        while idx_x < substitute_length(edges):
            triple = edges[idx_x]
            u_prime, v_prime, w_prime = triple
            push_to_list(graph[u_prime], (v_prime, w_prime))
            push_to_list(graph[v_prime], (u_prime, w_prime))
            idx_x += 1

        n_val = max(graph.keys()) + 1 if graph else 0
        result_lst = [0] * n_val

        def dfs(xs: int, yt: int, zd: int, ak: List[int]) -> int:
            if substitute_modulo(zd, signalSpeed) == 0:
                push_to_list(ak, xs)

            local_ctr = 0
            iter_list = graph[xs]
            iter_idx = 0
            while iter_idx < substitute_length(iter_list):
                tup_var = iter_list[iter_idx]
                neighbor_it, weight_it = tup_var
                if neighbor_it != yt:
                    local_ctr += dfs(neighbor_it, xs, zd + weight_it, ak)
                iter_idx += 1

            if substitute_modulo(zd, signalSpeed) == 0:
                return local_ctr + 1
            else:
                return local_ctr

        def count_pairs_through_c(ca: int) -> int:
            paths_accum = []
            neis = graph[ca]
            kk = 0
            while kk < substitute_length(neis):
                neighbor_p, weight_p = neis[kk]
                temp_path = []
                dfs(neighbor_p, ca, weight_p, temp_path)
                push_to_list(paths_accum, temp_path)
                kk += 1

            total_pair_sum = 0
            bb = 0
            while bb < (substitute_length(paths_accum) - 1):
                cc = bb + 1
                while cc < substitute_length(paths_accum):
                    len_bb = substitute_length(paths_accum[bb])
                    len_cc = substitute_length(paths_accum[cc])
                    total_pair_sum += len_bb * len_cc
                    cc += 1
                bb += 1
            return total_pair_sum

        outer_idx = 0
        while outer_idx < n_val:
            result_lst[outer_idx] = count_pairs_through_c(outer_idx)
            outer_idx += 1

        return result_lst