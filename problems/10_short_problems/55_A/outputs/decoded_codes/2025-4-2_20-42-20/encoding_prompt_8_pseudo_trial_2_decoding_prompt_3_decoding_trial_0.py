# Function to determine if all elements in a list can be marked as 'False'
def can_mark_all_false():
    # Step 1: Initialize Variables
    n = int(input())  # Read an integer value n from user input
    b = [True] * n    # Create a list of size n filled with True values
    j = 0             # Initialize index j to track list positions
    i = 1             # Initialize step counter i

    # Step 2: Iterate to Mark Values
    while i <= 500000:
        if b[j]:  # Check if the current index j in list b is True
            b[j] = False  # Mark the value at index j as False
        i += 1  # Increment the step counter
        j = (j + i) % n  # Update index j, wrapping around using modulo

    # Step 3: Check Remaining True Values
    if all(not value for value in b):  # Check if all values in b are False
        print("YES")
    else:
        print("NO")

# Invoking the function
can_mark_all_false()
