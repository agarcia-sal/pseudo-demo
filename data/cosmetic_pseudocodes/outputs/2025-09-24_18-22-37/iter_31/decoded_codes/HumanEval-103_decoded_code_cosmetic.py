def rounded_avg(alpha: int, beta: int) -> str | int:
    if beta >= alpha:
        total_sum = 0
        current = alpha
        while current <= beta:
            total_sum += current
            current += 1
        count_elements = (beta - alpha) + 1
        quotient = total_sum / count_elements
        nearest_int = round(quotient)
        binary_str = bin(nearest_int)[2:]
        return binary_str
    else:
        return -1