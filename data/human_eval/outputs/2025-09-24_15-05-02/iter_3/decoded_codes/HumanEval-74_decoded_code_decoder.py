def total_match(lst1, lst2):
    """
    Returns lst1 if the total length of strings in lst1 is less than or equal to 
    the total length of strings in lst2; otherwise, returns lst2.
    """
    total_length_1 = sum(len(s) for s in lst1)
    total_length_2 = sum(len(s) for s in lst2)

    return lst1 if total_length_1 <= total_length_2 else lst2