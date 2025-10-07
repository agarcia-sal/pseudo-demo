def digits(x: int) -> int:
    product_var: int = 1
    counter_odd: int = 0
    index: int = 0
    chars: str = str(x)
    while index < len(chars):
        num_val: int = int(chars[index])
        if num_val % 2 != 0:
            counter_odd += 1
            product_var *= num_val
        index += 1
    return 0 if counter_odd == 0 else product_var