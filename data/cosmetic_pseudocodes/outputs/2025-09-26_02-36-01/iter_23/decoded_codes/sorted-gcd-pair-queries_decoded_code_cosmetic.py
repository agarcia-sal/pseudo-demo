class Solution:
    def gcdValues(self, nums, queries):
        def helper_maximum(arr):
            def recursive_maximum(idx, val):
                if idx >= len(arr):
                    return val
                return recursive_maximum(idx + 1, arr[idx] if arr[idx] > val else val)
            return recursive_maximum(0, 0)

        def helper_count_elements(array):
            map_counter = {}
            def rec_count(pos):
                if pos >= len(array):
                    return
                map_counter[array[pos]] = map_counter.get(array[pos], 0) + 1
                rec_count(pos + 1)
            rec_count(0)
            return map_counter

        def zero_initialized_list(n):
            def recurse_fill(i, lst):
                if i >= n:
                    return lst
                lst[i] = 0
                return recurse_fill(i + 1, lst)
            return recurse_fill(0, [0] * n)

        def inner_loop(i_val, max_v, count_dict, cnt_g_lst):
            def inner_j_loop(j_val, accum_v):
                if j_val > max_v:
                    return accum_v
                updated_v = accum_v + count_dict.get(j_val, 0)
                cnt_g_lst[i_val] -= cnt_g_lst[j_val]
                return inner_j_loop(j_val + i_val, updated_v)
            return inner_j_loop(i_val, 0)

        def outer_loop(i, max_v, count_dict, cnt_g_lst):
            if i == 0:
                return
            temp_v = inner_loop(i, max_v, count_dict, cnt_g_lst)
            cnt_g_lst[i] += temp_v * (temp_v - 1) // 2
            outer_loop(i - 1, max_v, count_dict, cnt_g_lst)

        def accumulate_list(arr):
            def accumulate_rec(idx, acc, res_lst):
                if idx >= len(arr):
                    return res_lst
                res_lst[idx] = acc + arr[idx]
                return accumulate_rec(idx + 1, res_lst[idx], res_lst)
            return accumulate_rec(0, 0, [0]*len(arr))

        def bisect_right(array, val):
            def bisect_helper(lo, hi):
                if lo >= hi:
                    return lo
                mid = (lo + hi) // 2
                if val < array[mid]:
                    return bisect_helper(lo, mid)
                else:
                    return bisect_helper(mid + 1, hi)
            return bisect_helper(0, len(array))

        var_M = helper_maximum(nums)
        var_C = helper_count_elements(nums)
        var_G = zero_initialized_list(var_M + 1)
        outer_loop(var_M, var_M, var_C, var_G)
        var_S = accumulate_list(var_G)

        def process_queries(lst, qs, idx, acc_result):
            if idx >= len(qs):
                return acc_result
            pos_result = bisect_right(lst, qs[idx])
            return process_queries(lst, qs, idx + 1, acc_result + [pos_result])

        return process_queries(var_S, queries, 0, [])