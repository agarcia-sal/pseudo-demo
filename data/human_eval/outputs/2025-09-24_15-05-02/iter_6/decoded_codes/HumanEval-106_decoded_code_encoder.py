def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            product = 1
            for j in range(1, i + 1):
                product *= j
            result.append(product)
        else:
            total = 0
            for j in range(1, i + 1):
                total += j
            result.append(total)
    return result