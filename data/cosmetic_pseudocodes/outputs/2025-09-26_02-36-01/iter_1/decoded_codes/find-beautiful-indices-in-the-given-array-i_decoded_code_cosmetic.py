class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        found_a_positions = []
        s_length = len(s)
        a_length = len(a)
        b_length = len(b)

        for position in range(s_length - a_length + 1):
            if s[position:position + a_length] == a:
                found_a_positions.append(position)

        found_b_positions = []
        for position in range(s_length - b_length + 1):
            if s[position:position + b_length] == b:
                found_b_positions.append(position)

        result_indices = []
        for pos_a in found_a_positions:
            for pos_b in found_b_positions:
                if abs(pos_a - pos_b) <= k:
                    result_indices.append(pos_a)
                    break

        return result_indices