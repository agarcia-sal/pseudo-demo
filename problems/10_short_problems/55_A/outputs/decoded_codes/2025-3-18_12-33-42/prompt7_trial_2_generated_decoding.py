def check_numbers(n):
    # Initialize a boolean array with all elements set to True
    boolean_array = [True] * n
    
    # Initialize index and step variables
    index = 0
    step = 1

    # Iterate while step is less than or equal to 500000
    while step <= 500000:
        # If the current index is marked True, set it to False
        if boolean_array[index]:
            boolean_array[index] = False
        
        # Increment step
        step += 1
        
        # Update the index to point to the next position in the array in a circular manner
        index = (index + step) % n

    # Create a new list with only elements that remain True
    remaining_true = [i for i in boolean_array if i]

    # Check if there are no remaining True values
    if len(remaining_true) == 0:
        print("YES")  # Output "YES" if no True values are left
    else:
        print("NO")   # Output "NO" if there are True values remaining

# Input: Read an integer value n from the user
n = int(input())
check_numbers(n)
