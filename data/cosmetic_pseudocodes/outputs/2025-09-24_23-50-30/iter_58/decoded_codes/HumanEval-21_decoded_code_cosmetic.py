from typing import List

def rescale_to_unit(input_array: List[float]) -> List[float]:
    a = input_array
    b = a[0]
    c = a[0]
    for d in range(1, len(a)):
        if a[d] < b:
            b = a[d]
        if a[d] > c:
            c = a[d]
    e = c - b
    f: List[float] = []
    g = 0
    while g < len(a):
        h = (a[g] - b) / e
        f.append(h)
        g += 1
    return f