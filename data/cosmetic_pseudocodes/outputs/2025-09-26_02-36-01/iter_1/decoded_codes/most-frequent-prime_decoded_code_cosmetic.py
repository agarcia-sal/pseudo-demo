def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class Solution:
    def mostFrequentPrime(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        prime_freq = {}

        def explore(r, c, dr, dc, curr_num):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_num = curr_num * 10 + mat[nr][nc]
                if new_num > 10 and is_prime(new_num):
                    prime_freq[new_num] = prime_freq.get(new_num, 0) + 1
                explore(nr, nc, dr, dc, new_num)

        for row in range(rows):
            for col in range(cols):
                for dx, dy in steps:
                    explore(row, col, dx, dy, mat[row][col])

        if not prime_freq:
            return -1

        result = None
        highest_count = -1
        for num, count in prime_freq.items():
            if count > highest_count or (count == highest_count and num > result):
                highest_count = count
                result = num

        return result