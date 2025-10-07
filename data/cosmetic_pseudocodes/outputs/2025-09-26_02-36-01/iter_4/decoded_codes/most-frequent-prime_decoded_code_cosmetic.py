from collections import defaultdict

def is_prime(number: int) -> bool:
    threshold_one = 1
    threshold_three = 3
    divisor_two = 2
    divisor_three = 3
    current_candidate = 5
    step_increment = 6

    if not (number > threshold_one):
        return False
    elif number <= threshold_three:
        return True

    if (number % divisor_two == 0) or (number % divisor_three == 0):
        return False

    while current_candidate * current_candidate <= number:
        condition_one = number % current_candidate
        condition_two = number % (current_candidate + 2)
        if condition_one == 0 or condition_two == 0:
            return False
        current_candidate += step_increment

    return True

class Solution:
    def mostFrequentPrime(self, matrix: list[list[int]]) -> int:
        row_count = len(matrix)
        col_count = len(matrix[0]) if row_count > 0 else 0
        movement_vectors = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                            (1, 0), (1, -1), (0, -1), (-1, -1)]
        prime_occurrences = defaultdict(int)

        def traverse(x_coord: int, y_coord: int, delta_x: int, delta_y: int, accumulated_num: int) -> None:
            next_x = x_coord + delta_x
            next_y = y_coord + delta_y
            if 0 <= next_x < row_count and 0 <= next_y < col_count:
                extended_num = accumulated_num * 10 + matrix[next_x][next_y]
                if extended_num > 10 and is_prime(extended_num):
                    prime_occurrences[extended_num] += 1
                traverse(next_x, next_y, delta_x, delta_y, extended_num)

        row_index = 0
        while row_index < row_count:
            col_index = 0
            while col_index < col_count:
                vector_index = 0
                while vector_index < len(movement_vectors):
                    dx, dy = movement_vectors[vector_index]
                    starting_val = matrix[row_index][col_index]
                    traverse(row_index, col_index, dx, dy, starting_val)
                    vector_index += 1
                col_index += 1
            row_index += 1

        if not prime_occurrences:
            return -1

        max_frequency = -1
        candidate_prime = -1
        for prime_value, freq in prime_occurrences.items():
            if (freq > max_frequency) or (freq == max_frequency and prime_value > candidate_prime):
                max_frequency = freq
                candidate_prime = prime_value

        return candidate_prime