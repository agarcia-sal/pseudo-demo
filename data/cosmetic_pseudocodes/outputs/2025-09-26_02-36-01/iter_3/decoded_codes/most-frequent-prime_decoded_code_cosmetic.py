def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    counter = 5
    while counter * counter <= number:
        if number % counter == 0 or number % (counter + 2) == 0:
            return False
        counter += 6
    return True


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        vectors = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]
        frequency_map = {}

        def traverse(x_pos: int, y_pos: int, delta_x: int, delta_y: int, acc_num: int) -> None:
            next_x = x_pos + delta_x
            next_y = y_pos + delta_y
            if 0 <= next_x < rows and 0 <= next_y < cols:
                extended_num = acc_num * 10 + mat[next_x][next_y]
                if extended_num > 10 and is_prime(extended_num):
                    frequency_map[extended_num] = frequency_map.get(extended_num, 0) + 1
                traverse(next_x, next_y, delta_x, delta_y, extended_num)

        for row_idx in range(rows):
            for col_idx in range(cols):
                for dx, dy in vectors:
                    traverse(row_idx, col_idx, dx, dy, mat[row_idx][col_idx])

        if not frequency_map:
            return -1

        max_prime = None
        max_freq = -1
        for key, freq in frequency_map.items():
            if freq > max_freq or (freq == max_freq and (max_prime is None or key > max_prime)):
                max_prime = key
                max_freq = freq

        return max_prime