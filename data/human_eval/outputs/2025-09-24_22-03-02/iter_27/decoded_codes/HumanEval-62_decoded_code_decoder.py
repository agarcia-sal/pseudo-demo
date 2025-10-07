def derivative(xs: list) -> list:
    result = [0]
    length = len(xs)
    for index in range(length):
        term = index * xs[index]
        result.append(term)
    return result[1:len(result)-1]