def derivative(xs: list) -> list:
    result = [0]
    length = len(xs)
    for i in range(length):
        x = xs[i]
        value = i * x
        result.append(value)
    result.pop(0)
    return result