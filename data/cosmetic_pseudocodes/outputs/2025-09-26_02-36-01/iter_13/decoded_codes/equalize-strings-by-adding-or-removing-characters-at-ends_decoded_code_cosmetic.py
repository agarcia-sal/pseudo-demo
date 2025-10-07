class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        len_initial = 0
        len_target = 0
        max_length = 0
        dp_matrix = []

        def initialize_lengths():
            nonlocal len_initial, len_target
            len_initial = len(initial)
            len_target = len(target)

        def create_dp():
            nonlocal dp_matrix
            dp_matrix = [[0] * (len_target + 1) for _ in range(len_initial + 1)]

        def get_char_at_pos(s: str, pos: int) -> str:
            return s[pos]

        def compute_lcs(i: int, j: int):
            nonlocal max_length
            if i > len_initial:
                return
            if j > len_target:
                compute_next_i(i + 1)
                return
            if get_char_at_pos(initial, i - 1) == get_char_at_pos(target, j - 1):
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                if max_length < dp_matrix[i][j]:
                    max_length = dp_matrix[i][j]
            compute_lcs(i, j + 1)

        def compute_next_i(new_i: int):
            if new_i > len_initial:
                return
            compute_lcs(new_i, 1)

        initialize_lengths()
        create_dp()
        compute_next_i(1)

        result = (len_initial + len_target) - 2 * max_length
        return result