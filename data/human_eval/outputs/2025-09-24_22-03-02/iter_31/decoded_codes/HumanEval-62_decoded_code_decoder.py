def derivative(xs: list) -> list:
    result = [0]
    index = 0
    while index < len(xs):
        i = index
        x = xs[index]
        product = i * x
        result.append(product)
        index += 1
    sliced_result = []
    slice_index = 1
    while slice_index < len(result):
        sliced_result.append(result[slice_index])
        slice_index += 1
    return sliced_result