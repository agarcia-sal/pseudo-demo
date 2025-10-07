def derivative(xs):
    result = []
    for index in range(len(xs)):
        coefficient = xs[index]
        multiplied_value = index * coefficient
        result.append(multiplied_value)
    result = result[1:]
    return result