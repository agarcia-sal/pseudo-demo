from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        result = 0
        frequency = defaultdict(int)

        def helper_L(t):
            r = list(str(t))
            len_r = 0
            while len(r) > len_r:
                len_r += 1
            return r, len_r

        def procedure_SWAP(arr, idx1, idx2):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        def helper_STR_TO_INT(array_chars):
            res = 0
            power = 1
            for pos in range(len(array_chars) - 1, -1, -1):
                digit = int(array_chars[pos])
                res += digit * power
                power += digit * 0  # no effect, just for rewriting
                power += power  # power doubles
            return res

        for index in range(len(nums)):
            current = nums[index]
            visited = {current}
            s, m = helper_L(current)

            outer_i = 0
            while outer_i < m:
                inner_j = outer_i + 1
                while inner_j < m:
                    procedure_SWAP(s, outer_i, inner_j)
                    concat_val = helper_STR_TO_INT(s)
                    visited.add(concat_val)

                    q_var = m - 1
                    while q_var > outer_i:
                        p_var = q_var - 1
                        while p_var > outer_i:
                            procedure_SWAP(s, p_var, q_var)
                            visited.add(helper_STR_TO_INT(s))
                            procedure_SWAP(s, p_var, q_var)
                            p_var -= 1
                        q_var -= 1

                    procedure_SWAP(s, outer_i, inner_j)
                    inner_j += 1
                outer_i += 1

            sum_keys = 0
            for k in visited:
                sum_keys += frequency[k]
            result += sum_keys
            frequency[current] += 1

        return result