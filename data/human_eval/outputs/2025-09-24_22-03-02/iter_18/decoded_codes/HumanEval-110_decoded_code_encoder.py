def exchange(lst1, lst2):
    odd = sum(1 for x in lst1 if x % 2 == 1)
    even = sum(1 for x in lst2 if x % 2 == 0)
    if even >= odd:
        return "YES"
    return "NO"