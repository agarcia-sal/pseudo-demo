def get_odd_collatz(n):
    odd_collatz = [] if n % 2 == 0 else [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(n)
    odd_collatz = sorted(odd_collatz)
    return odd_collatz