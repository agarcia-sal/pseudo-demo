def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd = sum(1 for i in lst1 if i % 2 == 1)

    # Count the number of even elements in lst2
    even = sum(1 for i in lst2 if i % 2 == 0)

    # Return "YES" if even count >= odd count, else "NO"
    return "YES" if even >= odd else "NO"