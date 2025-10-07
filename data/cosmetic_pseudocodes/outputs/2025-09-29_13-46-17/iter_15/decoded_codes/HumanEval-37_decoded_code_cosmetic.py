from typing import List

def sort_even(lst: List[int]) -> List[int]:
    def extract(a: List[int], n: int, i: int, m: int) -> List[int]:
        if i >= m:
            return []
        return [a[i]] + extract(a, n, i + 2, m)
    even_elements = extract(lst, 0, 0, len(lst))
    odd_elements = extract(lst, 0, 1, len(lst))

    def merge(xs: List[int], ys: List[int]) -> List[int]:
        if not ys:
            return xs
        if not xs:
            return ys
        if ys[0] <= xs[0]:
            return [ys[0]] + merge(xs, ys[1:])
        else:
            return [xs[0]] + merge(xs[1:], ys)

    even_sorted = merge(even_elements, [])

    def assemble_rec(even_list: List[int], odd_list: List[int], _: int) -> List[int]:
        if not even_list and not odd_list:
            return []
        if not even_list:
            return odd_list
        if not odd_list:
            return even_list
        return [even_list[0], odd_list[0]] + assemble_rec(even_list[1:], odd_list[1:], 0)

    res = assemble_rec(even_sorted, odd_elements, 0)
    if len(even_sorted) > len(odd_elements):
        res.append(even_sorted[-1])
    return res