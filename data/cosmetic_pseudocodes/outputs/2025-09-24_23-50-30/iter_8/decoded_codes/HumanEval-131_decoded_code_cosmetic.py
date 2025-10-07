def digits(n: int) -> int:
    index: int = 0
    accumulator: int = 1
    counter: int = 0
    str_n: str = str(n)
    while index < len(str_n):
        tmp: int = int(str_n[index])
        if tmp % 2 != 0:
            accumulator *= tmp
            counter += 1
        index += 1
    return 0 if counter == 0 else accumulator