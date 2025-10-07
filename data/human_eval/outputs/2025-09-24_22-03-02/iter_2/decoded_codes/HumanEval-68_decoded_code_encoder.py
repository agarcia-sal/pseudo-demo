def pluck(arr):
    if len(arr) == 0:
        return []

    evens = [x for x in arr if x % 2 == 0]

    if not evens:
        return []

    smallest_value = min(evens)
    smallest_index = arr.index(smallest_value)

    return [smallest_value, smallest_index]