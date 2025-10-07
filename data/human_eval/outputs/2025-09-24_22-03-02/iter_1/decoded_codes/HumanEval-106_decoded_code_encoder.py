def factorial(k):
    result = 1
    for j in range(1, k + 1):
        result *= j
    return result

def f(n):
    return [factorial(i) if i % 2 == 0 else (i * (i + 1)) // 2 for i in range(1, n + 1)]