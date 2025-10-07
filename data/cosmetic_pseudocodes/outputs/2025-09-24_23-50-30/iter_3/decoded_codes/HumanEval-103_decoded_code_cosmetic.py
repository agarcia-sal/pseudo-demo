def rounded_avg(n: int, m: int) -> str:
    if n > m:
        return "-1"
    count: int = m - n + 1
    total: int = 0
    index: int = n
    for _ in range(count):
        total += index
        index += 1
    avg: float = total / count
    rounded: int = int((avg + 0.5) // 1)
    if rounded == 0:
        return "0"
    bin_str = ""
    number = rounded
    while number > 0:
        bin_str = str(number % 2) + bin_str
        number //= 2
    return bin_str