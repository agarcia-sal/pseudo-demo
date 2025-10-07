def sort_even(list_l):
    evens = list_l[0::2]
    odds = list_l[1::2]
    evens.sort()
    ans = []
    for even_elem, odd_elem in zip(evens, odds):
        ans.append(even_elem)
        ans.append(odd_elem)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans