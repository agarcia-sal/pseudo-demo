class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        length_initial = 0
        while length_initial < len(initial):
            length_initial += 1

        length_target = 0
        while length_target < len(target):
            length_target += 1

        row_count = length_initial + 1
        col_count = length_target + 1
        table = []
        index_row = 0
        while index_row < row_count:
            new_row = []
            index_col = 0
            while index_col < col_count:
                new_row.append(0)
                index_col += 1
            table.append(new_row)
            index_row += 1

        longest_subseq = 0
        outer_index = 1
        while outer_index <= length_initial:
            inner_index = 1
            while inner_index <= length_target:
                if not (initial[outer_index - 1] != target[inner_index - 1]):
                    temp_val = table[outer_index - 1][inner_index - 1] + 1
                    table[outer_index][inner_index] = temp_val
                    if longest_subseq < temp_val:
                        longest_subseq = temp_val
                inner_index += 1
            outer_index += 1

        return (length_initial + length_target) - (longest_subseq << 1)