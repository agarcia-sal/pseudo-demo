def exchange(lst1, lst2):
    odd = sum(1 for x in lst1 if x % 2 == 1)
    even = sum(1 for y in lst2 if y % 2 == 0)
    return "YES" if even >= odd else "NO"