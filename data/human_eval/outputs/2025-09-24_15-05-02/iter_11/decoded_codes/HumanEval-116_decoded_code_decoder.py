def sort_array(array):
    array.sort()  # sort by value ascending
    array.sort(key=lambda x: bin(x).count('1'))  # stable sort by count of '1' digits in binary representation
    return array