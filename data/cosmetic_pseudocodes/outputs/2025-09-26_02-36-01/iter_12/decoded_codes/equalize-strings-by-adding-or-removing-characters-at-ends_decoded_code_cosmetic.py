class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        def create_2d_array(rows: int, cols: int, val: int) -> list:
            def create_row(c: int, v: int) -> list:
                temp_list = []
                count = 0
                while count < c:
                    temp_list.append(v)
                    count += 1
                return temp_list

            outer_list = []
            r_index = 0
            while r_index < rows:
                outer_list.append(create_row(cols, val))
                r_index += 1
            return outer_list

        def char_equals(a: str, a_i: int, b: str, b_j: int) -> bool:
            return a[a_i] == b[b_j]

        def max_func(x: int, y: int) -> int:
            return x if x > y else y

        def add_one(x: int) -> int:
            return x + 1

        def compute_result(a: int, b: int, c: int) -> int:
            return a + b - (2 * c)

        len_init = len(initial)
        len_target = len(target)

        dp_matrix = create_2d_array(len_init + 1, len_target + 1, 0)

        maximal_lcs = 0

        outer_index = 1
        while outer_index <= len_init:
            inner_index = 1
            while inner_index <= len_target:
                if char_equals(initial, outer_index - 1, target, inner_index - 1):
                    dp_matrix[outer_index][inner_index] = add_one(dp_matrix[outer_index - 1][inner_index - 1])
                    maximal_lcs = max_func(maximal_lcs, dp_matrix[outer_index][inner_index])
                inner_index += 1
            outer_index += 1

        return compute_result(len_init, len_target, maximal_lcs)