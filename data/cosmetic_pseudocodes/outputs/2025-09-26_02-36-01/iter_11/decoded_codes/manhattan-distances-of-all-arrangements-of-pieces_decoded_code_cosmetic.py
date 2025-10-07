class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        modulus_value = 10**9 + 7

        def computeCombination(x: int, y: int) -> int:
            numerator_accumulator = 1
            denominator_accumulator = 1
            counter_outer = x
            counter_inner = 1
            while counter_inner <= y:
                numerator_accumulator *= counter_outer
                denominator_accumulator *= counter_inner
                counter_outer -= 1
                counter_inner += 1
            # Use integer division since numerator_accumulator and denominator_accumulator are integers
            return numerator_accumulator // denominator_accumulator

        def calculateContribution(size: int, MAXVAL=None) -> int:
            numerator = size * size * (size * size - size)
            return numerator // 6

        temp_alpha = n * n
        temp_beta = m * m

        first_component = calculateContribution(n)
        second_component = calculateContribution(m)

        total_combinations = computeCombination(m * n - 2, k - 2)

        cumulative_sum = (first_component * temp_beta + second_component * temp_alpha) * total_combinations
        answer_modulo = cumulative_sum % modulus_value

        return answer_modulo