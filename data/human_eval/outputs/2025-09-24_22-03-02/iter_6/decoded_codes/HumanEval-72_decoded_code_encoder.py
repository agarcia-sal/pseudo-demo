def will_it_fly(q, w):
    if sum(q) > w:
        return False
    left_index = 0
    right_index = len(q) - 1
    while left_index < right_index:
        if q[left_index] != q[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True