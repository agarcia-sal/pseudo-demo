def calculate(arr):
    if not arr:
        return None
    prod = 0 if 0 in arr else (-1) ** sum(1 for x in arr if x < 0)
    return prod * sum(abs(x) for x in arr)