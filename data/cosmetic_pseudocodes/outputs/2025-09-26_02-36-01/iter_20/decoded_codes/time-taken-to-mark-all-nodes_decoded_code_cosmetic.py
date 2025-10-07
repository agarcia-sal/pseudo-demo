from collections import deque
from typing import List, Tuple

class Solution:
    def timeTaken(self, edges: List[Tuple[int, int]]) -> List[int]:
        def _enqueue(tgt: int, tme: int, q: deque):
            q.append((tgt, tme))

        def _is_even(num: int) -> bool:
            return (num % 2) == 0

        def _make_visited(length: int) -> List[bool]:
            return [False] * length

        n = len(edges) + 1

        def _build_adj_list(items: List[Tuple[int,int]]) -> List[List[int]]:
            res = [[] for _ in range(n)]

            def _fill(i: int):
                if i >= len(items):
                    return
                a, b = items[i]
                res[a].append(b)
                res[b].append(a)
                _fill(i + 1)

            _fill(0)
            return res

        adj = _build_adj_list(edges)

        def _bfs(src: int) -> int:
            dq = deque()
            _enqueue(src, 0, dq)

            vis = _make_visited(n)
            vis[src] = True

            mx = 0

            while True:
                if not dq:
                    break
                cur, t = dq.popleft()
                if mx < t:
                    mx = t

                adjacent_size = len(adj[cur])

                def _process_neighbors(index: int):
                    if index >= adjacent_size:
                        return
                    nbr = adj[cur][index]
                    if not vis[nbr]:
                        vis[nbr] = True
                        if _is_even(nbr):
                            _enqueue(nbr, t + 2, dq)
                        else:
                            _enqueue(nbr, t + 1, dq)
                    _process_neighbors(index + 1)

                _process_neighbors(0)

            return mx

        result = []

        def _compute(i: int):
            if i >= n:
                return
            result.append(_bfs(i))
            _compute(i + 1)

        _compute(0)

        return result