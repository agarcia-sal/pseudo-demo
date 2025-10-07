def add_elements(arr, k):
    return sum(e for e in arr[:k] if len(str(e)) <= 2)