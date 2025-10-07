def smallest_change(array):
    return sum(array[i] != array[-i-1] for i in range(len(array)//2))