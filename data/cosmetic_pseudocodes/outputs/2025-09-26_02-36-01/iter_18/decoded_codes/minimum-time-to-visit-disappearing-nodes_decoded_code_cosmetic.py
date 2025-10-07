from typing import List, Tuple
from collections import defaultdict
import math

class Solution:
    def minimumTime(self, total: int, links: List[Tuple[int, int, int]], vanish: List[int]) -> List[int]:
        network = defaultdict(list)
        idx1 = 0
        while idx1 < len(links):
            src, dst, cost = links[idx1]

            network[src].append((dst, cost))
            network[dst].append((src, cost))

            idx1 += 1

        vals = [math.inf] * total
        vals[0] = 0

        heap = [(0, 0)]

        while len(heap) > 0:
            acc_dist, acc_node = self.pop_min_element(heap)

            if not (acc_dist < vanish[acc_node]):
                continue

            if acc_dist >= vals[acc_node]:
                continue

            adjacents = network[acc_node]
            idx2 = 0
            while idx2 < len(adjacents):
                nbr, wgt = adjacents[idx2]
                new_d = acc_dist + wgt
                if new_d >= vals[nbr] or new_d >= vanish[nbr]:
                    idx2 += 1
                    continue

                vals[nbr] = new_d
                self.insert_heap(heap, (new_d, nbr))
                idx2 += 1

        ans = [-1] * total
        pos = 0
        while pos < total:
            if vals[pos] < vanish[pos]:
                ans[pos] = vals[pos]
            pos += 1

        return ans

    def pop_min_element(self, h: List[Tuple[int, int]]) -> Tuple[int, int]:
        swap_finished = False
        last_index = len(h) - 1
        min_item = h[0]
        h[0] = h[last_index]
        h.pop()

        idx = 0
        while not swap_finished and idx * 2 + 1 < len(h):
            left_c = idx * 2 + 1
            right_c = idx * 2 + 2
            smallest = left_c

            if right_c < len(h) and h[right_c][0] < h[left_c][0]:
                smallest = right_c

            if h[idx][0] > h[smallest][0]:
                h[idx], h[smallest] = h[smallest], h[idx]
                idx = smallest
            else:
                swap_finished = True

        return min_item[0], min_item[1]

    def insert_heap(self, h: List[Tuple[int, int]], item: Tuple[int, int]) -> None:
        h.append(item)
        pos = len(h) - 1

        while pos > 0:
            parent = (pos - 1) // 2
            if h[parent][0] > h[pos][0]:
                h[parent], h[pos] = h[pos], h[parent]
                pos = parent
            else:
                break