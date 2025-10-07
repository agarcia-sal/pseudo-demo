class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        alpha_result = 0
        omega_length = 0
        delta_occurrences = 0
        auxiliary_sum = 0

        def count_occurrences(input_string: str, target_char: str) -> int:
            counter = 0
            index_iter = 0
            while index_iter < len(input_string):
                if input_string[index_iter] == target_char:
                    counter += 1
                index_iter += 1
            return counter

        delta_occurrences = count_occurrences(s, c)
        omega_length = len(s)
        auxiliary_sum = delta_occurrences + 1

        intermediate_value = 0

        def compute_half_sum(x: int) -> int:
            # Since the formula is (x * auxiliary_sum) / 2, and it seems integer arithmetic is expected
            return (x * auxiliary_sum) // 2

        intermediate_value = compute_half_sum(delta_occurrences)
        alpha_result = intermediate_value

        return alpha_result