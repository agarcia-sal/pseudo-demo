def exchange(lst1, lst2) -> str:
    odd = sum(1 for number in lst1 if number % 2 == 1)
    even = sum(1 for number in lst2 if number % 2 == 0)
    return "YES" if even >= odd else "NO"