class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s: str) -> int:
            alpha = 1
            omega = 0

            def update_max(current: int, max_ref: list):
                if max_ref[0] < current:
                    max_ref[0] = current

            def loop_check(i: int, max_ref: list, curr_len_ref: list):
                if s[i] == s[i - 1]:
                    curr_len_ref[0] += alpha
                else:
                    update_max(curr_len_ref[0], max_ref)
                    curr_len_ref[0] = alpha

            max_ref = [omega]
            curr_len_ref = [alpha]
            len_s = len(s)
            idx = alpha
            while idx < len_s:
                loop_check(idx, max_ref, curr_len_ref)
                idx += alpha
            # After loop, update max once more for the last sequence
            if max_ref[0] > curr_len_ref[0]:
                return max_ref[0]
            else:
                return curr_len_ref[0]

        def count_ones(x: int) -> int:
            count = 0
            temp = x
            while temp != 0:
                count += (temp & 1)
                temp >>= 1
            return count

        def flip_char(c: str) -> str:
            return '1' if c == '0' else '0'

        n = len(s)
        upper_bound = 1 << n
        minimum_length = n
        iteration_var = 0

        while True:
            if iteration_var >= upper_bound:
                break

            if count_ones(iteration_var) > numOps:
                iteration_var += 1
                continue

            def apply_flips(base_list: list[str], mask: int) -> list[str]:
                result_list = []
                pos = 0
                length = len(base_list)
                while pos < length:
                    if (mask & (1 << pos)) != 0:
                        result_list.append(flip_char(base_list[pos]))
                    else:
                        result_list.append(base_list[pos])
                    pos += 1
                return result_list

            base_list = list(s)
            candidate_str = ''.join(apply_flips(base_list, iteration_var))
            candidate_length = longest_uniform_substring(candidate_str)

            if minimum_length > candidate_length:
                minimum_length = candidate_length

            iteration_var += 1

        return minimum_length