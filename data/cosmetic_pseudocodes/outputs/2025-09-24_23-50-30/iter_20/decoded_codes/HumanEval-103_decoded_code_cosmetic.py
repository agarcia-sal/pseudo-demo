def rounded_avg(alpha: int, beta: int) -> str:
    if alpha > beta:
        return "-1"
    temp_sum = 0
    counter = alpha
    while counter <= beta:
        temp_sum += counter
        counter += 1
    count_elements = (beta - alpha) + 1
    parted_avg = temp_sum / count_elements
    final_avg = round(parted_avg)
    bin_out = bin(final_avg)[2:]
    return bin_out