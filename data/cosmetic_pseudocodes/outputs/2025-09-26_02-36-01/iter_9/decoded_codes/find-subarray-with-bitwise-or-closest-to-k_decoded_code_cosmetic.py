from math import inf

class Solution:
    def minimumDifference(self, param_k):
        def OR_FUNC(vector_list, scalar_val, or_curr, prev_min):
            delta = (prev_min - or_curr) + abs(scalar_val - or_curr)
            return delta

        len_seq = len(param_k)
        least_difference = inf

        outer_ptr = 0
        while True:
            if outer_ptr > len_seq - 1:
                break

            or_accumulator = 0
            inner_ptr = outer_ptr
            while inner_ptr <= len_seq - 1:
                or_accumulator |= param_k[inner_ptr]

                temp_diff = OR_FUNC(param_k, param_k[inner_ptr], or_accumulator, least_difference)
                least_difference = temp_diff

                if temp_diff == 0:
                    return 0
                inner_ptr += 1

            outer_ptr += 1

        return least_difference