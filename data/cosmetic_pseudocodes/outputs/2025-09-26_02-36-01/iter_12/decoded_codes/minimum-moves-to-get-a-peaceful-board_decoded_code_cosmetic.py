class Solution:
    def minMoves(self, rooks):
        def custom_abs(value):
            return -value if value < 0 else value

        def custom_sort_by_first_element(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[0]
            less = []
            greater = []
            equal = []
            for element in lst:
                if element[0] < pivot[0]:
                    less.append(element)
                elif element[0] > pivot[0]:
                    greater.append(element)
                else:
                    equal.append(element)
            return custom_sort_by_first_element(less) + equal + custom_sort_by_first_element(greater)

        def custom_sort_by_second_element(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[0]
            less = []
            greater = []
            equal = []
            for element in lst:
                if element[1] < pivot[1]:
                    less.append(element)
                elif element[1] > pivot[1]:
                    greater.append(element)
                else:
                    equal.append(element)
            return custom_sort_by_second_element(less) + equal + custom_sort_by_second_element(greater)

        length_rooks = 0
        while length_rooks < len(rooks) and rooks[length_rooks] is not None:
            length_rooks += 1

        sorted_rooks_row = custom_sort_by_first_element(rooks[:length_rooks])
        sorted_rooks_col = custom_sort_by_second_element(rooks[:length_rooks])

        total_row_moves = 0
        for pos_row_index in range(length_rooks):
            delta = sorted_rooks_row[pos_row_index][0]
            index_diff = pos_row_index
            diff_value = (delta + ((index_diff * (-1)) + index_diff)) - index_diff
            abs_diff = custom_abs(diff_value)
            total_row_moves += abs_diff

        total_col_moves = 0
        pos_col_index = 0
        while pos_col_index < length_rooks:
            delta_col = sorted_rooks_col[pos_col_index][1]
            index_diff_col = pos_col_index
            diff_val_col = delta_col - index_diff_col
            abs_diff_col = diff_val_col - (2 * diff_val_col) if diff_val_col < 0 else diff_val_col
            total_col_moves += abs_diff_col
            pos_col_index += 1

        return total_row_moves + total_col_moves