def exchange(lst1, lst2):
    odd = sum(i % 2 == 1 for i in lst1)
    even = sum(i % 2 == 0 for i in lst2)
    return "YES" if even >= odd else "NO"