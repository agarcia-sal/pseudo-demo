def count_nums(arr: list[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        n_digits = [int(ch) for ch in str(n)]
        n_digits[0] *= neg
        sum_digits = sum(n_digits)
        return sum_digits

    filtered_sums = []
    for i in range(len(arr)):
        ds = digits_sum(arr[i])
        if ds > 0:
            filtered_sums.append(ds)
    return len(filtered_sums)