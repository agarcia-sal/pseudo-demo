def solution(lst):
    # Sum elements at even indices that are also odd numbers
    return sum(x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1)