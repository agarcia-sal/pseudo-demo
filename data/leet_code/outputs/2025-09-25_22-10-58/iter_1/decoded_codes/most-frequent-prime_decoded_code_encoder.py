def is_prime(n: int) -> bool:
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
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]
        prime_count = {}

        def traverse(x: int, y: int, dx: int, dy: int, current_number: int) -> None:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_number = current_number * 10 + mat[nx][ny]
                if new_number > 10 and is_prime(new_number):
                    prime_count[new_number] = prime_count.get(new_number, 0) + 1
                traverse(nx, ny, dx, dy, new_number)

        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    traverse(i, j, dx, dy, mat[i][j])

        if not prime_count:
            return -1
        # max by count and then by prime value (if tie)
        most_frequent_prime = max(prime_count.items(), key=lambda item: (item[1], item[0]))[0]
        return most_frequent_prime