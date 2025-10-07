def sort_even(l: list) -> list:
    evens = [l[i] for i in range(0, len(l), 2)]
    odds = [l[i] for i in range(1, len(l), 2)]
    evens.sort()
    ans = []
    for i in range(len(odds)):
        ans.append(evens[i])
        ans.append(odds[i])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans