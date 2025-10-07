class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def length_of_string(x: str) -> int:
            count = 0
            while True:
                try:
                    _ = x[count]
                except IndexError:
                    break
                count += 1
            return count

        def substring_equal(str_main: str, start_pos: int, comparison_str: str) -> bool:
            l = length_of_string(comparison_str)
            pos = 0
            while pos < l:
                if str_main[start_pos + pos] != comparison_str[pos]:
                    return False
                pos += 1
            return True

        def gather_indices(source_str: str, pattern: str) -> list[int]:
            collected_indices = []
            source_len = length_of_string(source_str)
            pattern_len = length_of_string(pattern)

            def recursive_index_search(current_idx: int):
                if current_idx > source_len - pattern_len:
                    return
                if substring_equal(source_str, current_idx, pattern):
                    collected_indices.append(current_idx)
                recursive_index_search(current_idx + 1)

            recursive_index_search(0)
            return collected_indices

        indices_a_list = gather_indices(s, a)
        indices_b_list = gather_indices(s, b)

        result_indices = []

        def find_and_append(i_idx: int):
            def inner_search(j_idx: int) -> bool:
                if j_idx >= length_of_string(indices_b_list):
                    return False
                diff_abs = abs(indices_a_list[i_idx] - indices_b_list[j_idx])
                if diff_abs <= k:
                    result_indices.append(indices_a_list[i_idx])
                    return True
                return inner_search(j_idx + 1)
            inner_search(0)

        def i_loop(pos: int):
            if pos >= length_of_string(indices_a_list):
                return
            find_and_append(pos)
            i_loop(pos + 1)

        i_loop(0)
        return result_indices