def power(base: int, exp: int) -> int:
    return base ** exp

def prod_signs(arr):
    if not arr:
        return None
    prod = 0 if 0 in arr else power(-1, len([x for x in arr if x < 0]))
    return prod * sum(abs(x) for x in arr)