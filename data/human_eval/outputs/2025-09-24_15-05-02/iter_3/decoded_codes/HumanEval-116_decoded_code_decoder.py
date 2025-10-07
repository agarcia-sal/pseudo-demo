def sort_array(arr):
    """
    Sorts the input array in ascending order based on:
    1. The number of ones in the binary representation of each element.
    2. The decimal value of the element.
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))