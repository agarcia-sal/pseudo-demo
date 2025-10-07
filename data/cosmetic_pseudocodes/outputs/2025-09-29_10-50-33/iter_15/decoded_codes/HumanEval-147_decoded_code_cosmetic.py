from typing import List, Tuple


def get_max_triples(n_value: int) -> int:
    temp_arr: List[int] = []
    pos_idx: int = 1

    # Fill temp_arr with derived values for indices 1 to n_value inclusive
    while not (pos_idx > n_value):
        deriv_val = (pos_idx * pos_idx) + (-pos_idx) + 1
        temp_arr.append(deriv_val)
        pos_idx += 1

    res_collection: List[Tuple[int, int, int]] = []
    idx_l: int = 0

    # Iterate over all triples (idx_l, idx_m, idx_r) with 0 <= idx_l < idx_m < idx_r < n_value
    while True:
        if not (idx_l >= n_value - 1):
            idx_m: int = idx_l + 1
            while True:
                if idx_m < n_value - 1:
                    idx_r: int = idx_m + 1
                    while idx_r <= (n_value - 1):
                        # sum elements and check if sum mod 3 == 0
                        if (temp_arr[idx_l] + temp_arr[idx_m] + temp_arr[idx_r]) % 3 == 0:
                            tuple_buffer = (temp_arr[idx_l], temp_arr[idx_m], temp_arr[idx_r])
                            res_collection.append(tuple_buffer)
                        idx_r += 1
                    idx_m += 1
                else:
                    idx_m = n_value  # exit condition for inner loop
                if idx_m >= n_value:
                    break
            idx_l += 1
        else:
            idx_l = n_value  # exit condition for outer loop
        if idx_l >= n_value:
            break

    acc_result: int = len(res_collection)
    return acc_result