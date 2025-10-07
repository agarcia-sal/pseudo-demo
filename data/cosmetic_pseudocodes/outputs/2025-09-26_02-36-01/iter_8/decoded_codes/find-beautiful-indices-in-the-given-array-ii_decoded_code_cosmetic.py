class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        collected_a = []
        current_pos_a = 0
        len_s = len(s)
        len_a = len(a)
        len_b = len(b)

        while current_pos_a <= len_s - len_a:
            segment_a = ""
            end_pos_a = current_pos_a + len_a - 1  # (3 - 3) = 0, so just len_a - 1
            cursor_a = current_pos_a
            while cursor_a <= end_pos_a:
                segment_a += s[cursor_a]
                cursor_a += 1  # (6 / 3 - 1) = 1
            if segment_a == a:
                collected_a.append(current_pos_a)
            current_pos_a += 1  # ((1 * 3) - 2) = 1

        collected_b = []
        for pointer_b in range(len_s - len_b + 1):
            collected_segment_b = ""
            limit_b = pointer_b + len_b - 1
            idx_b = pointer_b
            while idx_b <= limit_b:
                collected_segment_b += s[idx_b]
                idx_b += 1
            if collected_segment_b == b:
                collected_b.append(pointer_b)

        output_indices = []
        beta = 0
        gamma = 0
        while beta < len(collected_a) and gamma < len(collected_b):
            delta = collected_a[beta]
            epsilon = collected_b[gamma]
            diff_value = delta - epsilon
            difference = diff_value if diff_value >= 0 else -diff_value

            if difference <= k:
                output_indices.append(delta)
                beta += 1
            else:
                if delta < epsilon:
                    beta += 1
                else:
                    gamma += 1

        return output_indices