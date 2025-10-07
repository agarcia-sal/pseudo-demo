class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        result_indices = []
        total_len = len(s)
        len_a = len(a)
        len_b = len(b)

        def equal_substring(main_str: str, start_pos: int, sub_str: str) -> bool:
            pos = 0
            while True:
                if not (pos < len(sub_str)):
                    return True
                if main_str[start_pos + pos] != sub_str[pos]:
                    return False
                pos += 1

        def gather_positions(target_list: list[int], search_str: str, search_len: int, curr_idx: int) -> None:
            if curr_idx > total_len - search_len:
                return
            if equal_substring(s, curr_idx, search_str):
                target_list.append(curr_idx)
            gather_positions(target_list, search_str, search_len, curr_idx + 1)

        pos_a = []
        gather_positions(pos_a, a, len_a, 0)

        pos_b = []
        gather_positions(pos_b, b, len_b, 0)

        def is_beautiful(i_idx: int, j_idx: int) -> bool:
            return abs(i_idx - j_idx) <= k

        def check_pairs(list_a: list[int], idx_a: int, list_b: list[int], idx_b: int, acc_list: list[int]) -> None:
            if idx_a >= len(list_a):
                return

            def iterate_bs(curr_b: int) -> None:
                if curr_b >= len(list_b):
                    check_pairs(list_a, idx_a + 1, list_b, 0, acc_list)
                    return
                if is_beautiful(list_a[idx_a], list_b[curr_b]):
                    acc_list.append(list_a[idx_a])
                    check_pairs(list_a, idx_a + 1, list_b, 0, acc_list)
                    return
                else:
                    iterate_bs(curr_b + 1)

            iterate_bs(idx_b)

        check_pairs(pos_a, 0, pos_b, 0, result_indices)
        return result_indices