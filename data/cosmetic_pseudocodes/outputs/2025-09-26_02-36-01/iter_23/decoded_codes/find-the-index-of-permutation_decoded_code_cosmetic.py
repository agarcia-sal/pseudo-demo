class Solution:
    def getPermutationIndex(self, perm):
        n_val = len(perm)
        mod_val = 10 ** 9 + 1

        fact_arr = [1] * n_val

        def build_factorial_array(count, arr):
            if count < 1:
                return
            arr[0] = 1
            def fill_factorial(cur, end_val, arr):
                if cur > end_val:
                    return
                arr[cur] = arr[cur - 1] * cur
                fill_factorial(cur + 1, end_val, arr)
            fill_factorial(1, count - 1, arr)

        build_factorial_array(n_val, fact_arr)

        num_list = []
        def build_number_list(size, list_ref):
            idx = 1
            while idx <= size:
                list_ref.append(idx)
                idx += 1

        build_number_list(n_val, num_list)

        res_idx = 0

        def compute_index(current, limit, perm_ref, num_ref, fact_ref, acc_index):
            if current == limit:
                return acc_index
            curr_val = perm_ref[current]

            j_val = 0
            length_val = len(num_ref)

            def find_position(val, lst, length_val, pos_acc):
                nonlocal j_val
                if j_val >= length_val:
                    return pos_acc
                if lst[j_val] == val:
                    return pos_acc
                j_val += 1
                return find_position(val, lst, length_val, pos_acc + 1)

            p_pos = find_position(curr_val, num_ref, length_val, 0)
            acc_index += p_pos * fact_ref[limit - current - 1]
            num_ref.pop(p_pos)

            return compute_index(current + 1, limit, perm_ref, num_ref, fact_ref, acc_index)

        res_idx = compute_index(0, n_val, perm, num_list, fact_arr, res_idx)
        result_val = res_idx % mod_val

        return result_val