def sort_third(lst):
    # Create a copy of the list to avoid mutating the input
    result = list(lst)

    # Extract elements at indices divisible by 3
    indices = [i for i in range(len(result)) if i % 3 == 0]
    elements = [result[i] for i in indices]

    # Sort the extracted elements
    elements.sort()

    # Assign sorted elements back to their original positions
    for i, val in zip(indices, elements):
        result[i] = val

    return result