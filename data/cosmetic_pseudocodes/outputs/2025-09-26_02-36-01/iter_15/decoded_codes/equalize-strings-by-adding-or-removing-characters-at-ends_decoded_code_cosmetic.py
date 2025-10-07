class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        alpha = len(initial)
        beta = len(target)
        matrix = [[0] * (beta + 1) for _ in range(alpha + 1)]
        peak_match = 0

        for outer_index in range(1, alpha + 1):
            for inner_index in range(1, beta + 1):
                if initial[outer_index - 1] == target[inner_index - 1]:
                    matrix[outer_index][inner_index] = matrix[outer_index - 1][inner_index - 1] + 1
                    if peak_match < matrix[outer_index][inner_index]:
                        peak_match = matrix[outer_index][inner_index]

        return alpha + beta - 2 * peak_match