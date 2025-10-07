class Solution:
    def beautifulIndices(self, s: str, param_a: str, param_b: str, max_diff: int) -> list[int]:
        a_positions = []
        pos1 = 0
        len_a = len(param_a)
        len_s = len(s)
        while pos1 <= len_s - len_a:
            segment = s[pos1: pos1 + len_a]
            if segment == param_a:
                a_positions.append(pos1)
            pos1 += 1

        b_positions = []
        pos2 = 0
        len_b = len(param_b)
        while pos2 <= len_s - len_b:
            segment_b = s[pos2: pos2 + len_b]
            if segment_b == param_b:
                b_positions.append(pos2)
            pos2 += 1

        result_indices = []
        idx_a = 0
        idx_b = 0
        while idx_a < len(a_positions) and idx_b < len(b_positions):
            dist = abs(a_positions[idx_a] - b_positions[idx_b])
            if dist <= max_diff:
                result_indices.append(a_positions[idx_a])
                idx_a += 1
            elif a_positions[idx_a] < b_positions[idx_b]:
                idx_a += 1
            else:
                idx_b += 1

        return result_indices