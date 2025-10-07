def digits(n: int) -> int:
    result: int = 1
    counter: int = 0
    digits_str: str = str(n)
    index: int = 0
    while index < len(digits_str):
        value: int = int(digits_str[index])
        if value % 2 == 1:
            result *= value
            counter += 1
        index += 1
    return 0 if counter == 0 else result