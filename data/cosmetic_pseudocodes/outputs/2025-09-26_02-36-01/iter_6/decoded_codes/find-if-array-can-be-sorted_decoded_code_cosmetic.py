class Solution:
    def canSortArray(self, ent_list):
        # Counts the number of set bits in val using tail-recursive helper
        def bit_count(val):
            def bit_count_rec(x, acc):
                if x <= 0:
                    return acc
                else:
                    return bit_count_rec(x // 2, acc + (x % 2))
            return bit_count_rec(val, 0)

        length_val = 0
        while True:
            try:
                _ = ent_list[length_val]
            except IndexError:
                break
            length_val += 1

        copy_list = []
        idx_a = 0
        while idx_a < length_val:
            copy_list.append(ent_list[idx_a])
            idx_a += 1

        def sort_asc(list_in):
            # Returns index of minimum element in arr[from_idx..to_idx]
            def min_index(from_idx, to_idx, arr, curr_min_idx):
                if from_idx > to_idx:
                    return curr_min_idx
                else:
                    if arr[from_idx] < arr[curr_min_idx]:
                        return min_index(from_idx + 1, to_idx, arr, from_idx)
                    else:
                        return min_index(from_idx + 1, to_idx, arr, curr_min_idx)

            def swap_elements(arr_temp, pos_x, pos_y):
                arr_temp[pos_x], arr_temp[pos_y] = arr_temp[pos_y], arr_temp[pos_x]
                return arr_temp

            def selection_sort_rec(start_idx, end_idx, arr_sort):
                if start_idx >= end_idx:
                    return arr_sort
                else:
                    min_pos = min_index(start_idx + 1, end_idx, arr_sort, start_idx)
                    if min_pos != start_idx:
                        arr_sort = swap_elements(arr_sort, start_idx, min_pos)
                    return selection_sort_rec(start_idx + 1, end_idx, arr_sort)

            return selection_sort_rec(0, len(list_in) - 1, list_in)

        sorted_vals = sort_asc(copy_list)

        # Recursive bubble sort with bit count stability condition
        def bubble_recursive(i_val, j_val, arr_check, max_idx):
            if i_val >= max_idx:
                return arr_check
            else:
                if j_val >= max_idx - i_val:
                    return bubble_recursive(i_val + 1, 0, arr_check, max_idx)
                else:
                    count_j = bit_count(arr_check[j_val])
                    count_jp = bit_count(arr_check[j_val + 1])
                    # Swap if bit counts are equal and arr_check[j_val] > arr_check[j_val + 1]
                    if (count_j == count_jp) and (arr_check[j_val] > arr_check[j_val + 1]):
                        arr_check[j_val], arr_check[j_val + 1] = arr_check[j_val + 1], arr_check[j_val]
                    return bubble_recursive(i_val, j_val + 1, arr_check, max_idx)

        result_arr = bubble_recursive(0, 0, ent_list[:], length_val)

        flag_eq = True
        idx_c = 0
        while idx_c < length_val:
            if result_arr[idx_c] != sorted_vals[idx_c]:
                flag_eq = False
                break
            idx_c += 1

        return flag_eq