class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        list_a_indices = []
        len_s = len(s)
        len_a = len(a)
        pos = 0
        while pos <= len_s - len_a:
            sub_s = s[pos:pos + len_a]
            if sub_s == a:
                list_a_indices.append(pos)
            pos += 1

        list_b_indices = []
        len_b = len(b)
        pos = 0
        while pos <= len_s - len_b:
            sub_str = s[pos:pos + len_b]
            if sub_str == b:
                list_b_indices.append(pos)
            pos += 1

        result_indices = []
        idx_a_pos = 0
        len_b_indices = len(list_b_indices)
        while idx_a_pos < len(list_a_indices):
            current_i = list_a_indices[idx_a_pos]
            idx_b_pos = 0
            found_flag = False
            while idx_b_pos < len_b_indices and not found_flag:
                current_j = list_b_indices[idx_b_pos]
                diff = current_i - current_j
                if -k <= diff <= k:
                    result_indices.append(current_i)
                    found_flag = True
                idx_b_pos += 1
            idx_a_pos += 1

        return result_indices