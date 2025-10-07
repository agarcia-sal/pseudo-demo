def get_odd_collatz(n):
    odd_collatz = [n] if n % 2 == 1 else []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    sorted_odd_collatz = sorted(odd_collatz)
    return sorted_odd_collatz