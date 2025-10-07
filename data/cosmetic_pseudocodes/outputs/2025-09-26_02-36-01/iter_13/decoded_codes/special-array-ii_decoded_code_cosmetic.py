class Solution:
    def isArraySpecial(self, nums, queries):
        def mod_two(x):
            return x - 2 * (x // 2)

        def zero_list(n):
            if n == 0:
                return []
            return [0] + zero_list(n - 1)

        def get_parity_list(arr, idx, acc):
            if idx == len(arr):
                return acc
            return get_parity_list(arr, idx + 1, acc + [mod_two(arr[idx])])

        parity = get_parity_list(nums, 0, [])

        prefix_special = zero_list(len(nums))

        def compute_prefix(lst, idx):
            if idx == len(lst):
                return
            diff_cond = (lst[idx] == lst[idx - 1])
            prefix_special[idx] = prefix_special[idx - 1] + (1 if diff_cond else 0)
            compute_prefix(lst, idx + 1)

        if len(nums) > 1:
            compute_prefix(parity, 1)

        def check_query(s, e):
            if s == e:
                return True
            left_value = prefix_special[s] if s > 0 else 0
            diff = prefix_special[e] - left_value
            return diff == 0

        def recur_queries(query_list, index, acc):
            if index == len(query_list):
                return acc
            current = query_list[index]
            acc.append(check_query(current[0], current[1]))
            return recur_queries(query_list, index + 1, acc)

        result = recur_queries(queries, 0, [])
        return result