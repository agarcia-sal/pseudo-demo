def can_mark_all_false(n):
    # Initialize the list with 'True' values
    b = [True] * n  
    j = 0  # Current index in the list
    i = 1  # Steps to take

    # Iterate to mark values until i reaches 500,000
    while i <= 500000:
        if b[j]:  # Check if the current index is 'True'
            b[j] = False  # Mark this position as 'False'
        i += 1  # Increment steps
        j = (j + i) % n  # Update index and wrap around using modulo if necessary

    # Check for remaining 'True' values in the list
    remaining_true_values = [value for value in b if value]
    
    # Determine and output the result
    return "YES" if len(remaining_true_values) == 0 else "NO"

# Read input and call the function
n = int(input())
result = can_mark_all_false(n)
print(result)
