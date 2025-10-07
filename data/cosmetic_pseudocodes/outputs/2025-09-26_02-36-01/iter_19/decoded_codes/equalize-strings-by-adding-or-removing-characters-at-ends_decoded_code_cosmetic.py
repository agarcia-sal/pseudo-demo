class Solution:
    def minOperations(self, init_str: str, goal_str: str) -> int:
        alpha = len(init_str)
        beta = len(goal_str)
        matrix = [[0] * (beta + 1) for _ in range(alpha + 1)]
        longest_match = 0
        outer_idx = 1
        while outer_idx <= alpha:
            inner_idx = 1
            while inner_idx <= beta:
                if init_str[outer_idx - 1] == goal_str[inner_idx - 1]:
                    previous_value = matrix[outer_idx - 1][inner_idx - 1]
                    matrix[outer_idx][inner_idx] = previous_value + 1
                    if longest_match < matrix[outer_idx][inner_idx]:
                        longest_match = matrix[outer_idx][inner_idx]
                inner_idx += 1
            outer_idx += 1
        result = (alpha + beta) - (2 * longest_match)
        return result