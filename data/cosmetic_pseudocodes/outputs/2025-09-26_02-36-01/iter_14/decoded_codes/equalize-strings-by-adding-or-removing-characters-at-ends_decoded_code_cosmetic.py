class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        first_length = 0
        traverse_index = 1
        while traverse_index <= len(initial):
            first_length += 1
            traverse_index += 1

        second_length = 0
        iterator_j = 1
        while iterator_j <= len(target):
            second_length += 1
            iterator_j += 1

        def createZeroGrid(rows: int, cols: int) -> list:
            outer_list = []
            row_counter = 0
            while True:
                if row_counter == rows:
                    break
                inner_list = []
                col_counter = 0
                while True:
                    if col_counter == cols:
                        break
                    inner_list.append(0)
                    col_counter += 1
                outer_list.append(inner_list)
                row_counter += 1
            return outer_list

        dp_matrix = createZeroGrid(first_length + 1, second_length + 1)
        max_lcs = 0

        outer_i = 1
        while True:
            if outer_i > first_length:
                break

            inner_j = 1
            while True:
                if inner_j > second_length:
                    break

                if not (initial[outer_i - 1] != target[inner_j - 1]):
                    dp_matrix[outer_i][inner_j] = dp_matrix[outer_i - 1][inner_j - 1] + 1
                    if dp_matrix[outer_i][inner_j] > (0 + max_lcs):
                        max_lcs = dp_matrix[outer_i][inner_j]

                inner_j += 1

            outer_i += 1

        return (first_length + second_length) - (2 * max_lcs)