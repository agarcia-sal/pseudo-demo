def add_elements(arr, k):
    return sum(element for element in arr[:k] if len(str(abs(element))) <= 2)