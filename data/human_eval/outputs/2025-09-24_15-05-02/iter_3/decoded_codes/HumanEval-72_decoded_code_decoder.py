def will_it_fly(q, w):
    # Check if sum of elements in q is greater than w
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1

    # Check if q is a palindrome
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1

    return True