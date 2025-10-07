def get_odd_collatz(n):
    odd_collatz = [n] if n % 2 else []
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        if n % 2 == 1:
            odd_collatz.append(n)
    return sorted(odd_collatz)