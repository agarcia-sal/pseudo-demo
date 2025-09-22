# Function to process the boolean list based on given conditions
def process_boolean_list():
    # Step 1: Input the size of the array
    n = int(input())  # Read the size of the array

    # Step 2: Initialize a list with True values
    boolean_list = [True] * n  # Create a list of size n, all set to True

    # Step 3: Initialize variables for looping
    j = 0  # Index for the boolean list
    i = 1  # Counter for the loop

    # Step 4: Loop to process values while i is less than or equal to 500000
    while i <= 500000:
        # If the current position j in the list boolean_list is True
        if boolean_list[j]:
            boolean_list[j] = False  # Mark position j as False

        # Move to the next value
        i += 1
        j = (j + i) % n  # Update position j using modulo operation to wrap around

    # Step 5: Create a new list x containing only True values from boolean_list
    true_values = [value for value in boolean_list if value]  # List of True values

    # Step 6: Check if the list true_values is empty and print the result
    if len(true_values) == 0:
        print("YES")  # No True values left in boolean_list
    else:
        print("NO")   # There are still True values in boolean_list

# Run the function
process_boolean_list()
