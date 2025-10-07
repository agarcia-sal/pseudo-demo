class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        len_s = len(s)
        len_a = len(a)
        len_b = len(b)
        positions_a = []
        positions_b = []

        idx1 = 0
        while idx1 <= len_s - len_a:
            if s[idx1:idx1 + len_a] == a:
                positions_a.append(idx1)
            idx1 += 1

        idx2 = 0
        while idx2 <= len_s - len_b:
            if s[idx2:idx2 + len_b] == b:
                positions_b.append(idx2)
            idx2 += 1

        result = []
        idx_a_ptr = 0

        while idx_a_ptr < len(positions_a):
            current_a = positions_a[idx_a_ptr]
            idx_b_ptr = 0
            while True:
                if idx_b_ptr >= len(positions_b):
                    break
                current_b = positions_b[idx_b_ptr]
                if abs(current_a - current_b) <= k:
                    result.append(current_a)
                    break
                idx_b_ptr += 1
            idx_a_ptr += 1

        return result