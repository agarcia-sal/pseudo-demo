def derivative(xs: list):
    result = [0]
    for i in range(len(xs) - 1):
        x = xs[i]
        value = i * x
        result.append(value)
    result = result[1:len(result) - 1]
    return result