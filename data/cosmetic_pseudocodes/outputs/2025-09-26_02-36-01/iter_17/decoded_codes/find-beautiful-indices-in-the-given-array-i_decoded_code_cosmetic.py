class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        temp_list_one = []
        original_len_s = len(s)
        original_len_a = len(a)
        step_counter_one = 0

        while step_counter_one <= original_len_s - original_len_a:
            current_fragment = s[step_counter_one:step_counter_one + original_len_a]
            if current_fragment == a:
                temp_list_one.append(step_counter_one)
            step_counter_one += 1

        temp_list_two = []
        original_len_b = len(b)
        step_counter_two = 0

        while step_counter_two <= original_len_s - original_len_b:
            current_fragment_two = s[step_counter_two:step_counter_two + original_len_b]
            if current_fragment_two == b:
                temp_list_two.append(step_counter_two)
            step_counter_two += 1

        result_indices = []
        outer_index = 0

        while outer_index < len(temp_list_one):
            inner_index = 0
            while inner_index < len(temp_list_two):
                diff_val = temp_list_one[outer_index] - temp_list_two[inner_index]
                if -k <= diff_val <= k:
                    result_indices.append(temp_list_one[outer_index])
                    break
                inner_index += 1
            outer_index += 1

        return result_indices