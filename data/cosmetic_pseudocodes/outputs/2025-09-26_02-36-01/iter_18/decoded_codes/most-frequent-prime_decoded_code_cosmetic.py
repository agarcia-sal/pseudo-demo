from typing import List, Tuple, Dict

def is_prime(alpha: int) -> bool:
    if alpha <= 1:
        return False
    if alpha <= 3:
        return True
    if alpha % 2 == 0 or alpha % 3 == 0:
        return False
    theta = 5
    while theta * theta <= alpha:
        if alpha % theta == 0 or alpha % (theta + 2) == 0:
            return False
        theta += 6
    return True

class Solution:
    def mostFrequentPrime(self, matrix: List[List[int]]) -> int:
        delta_a = len(matrix)
        delta_b = len(matrix[0])
        trajectory: List[Tuple[int, int]] = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        tally_map: Dict[int, int] = {}

        def voyage(p: int, q: int, r: int, s: int, val: int) -> None:
            nex_p = p + r
            nex_q = q + s
            if 0 <= nex_p < delta_a and 0 <= nex_q < delta_b:
                constructed = val * 10 + matrix[nex_p][nex_q]
                if constructed > 10 and is_prime(constructed):
                    tally_map[constructed] = tally_map.get(constructed, 0) + 1
                voyage(nex_p, nex_q, r, s, constructed)

        for bunk_a in range(delta_a):
            for bunk_b in range(delta_b):
                for rdx, rdy in trajectory:
                    voyage(bunk_a, bunk_b, rdx, rdy, matrix[bunk_a][bunk_b])

        if not tally_map:
            return -1

        peak_val = -1
        peak_key = -1
        for key, val in tally_map.items():
            if val > peak_val or (val == peak_val and key > peak_key):
                peak_val = val
                peak_key = key
        return peak_key