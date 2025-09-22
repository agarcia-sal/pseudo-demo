# Function to process the algorithm as described in the pseudocode
def process_values():
    # Step 1: Input the size of the array
    n = int(input())  # Read an integer input for the size of the array

    # Step 2: Initialize a boolean list with True values
    b = [True] * n  # List of size n, initialized with True

    # Step 3: Initialize variables for looping
    j = 0  # This will be our index into list b
    i = 1  # Starting value of i

    # Step 4: Loop to process values while i is less than or equal to 500000
    while i <= 500000:
        # If the current position j in the list b is True
        if b[j]:  # b[j] is equivalent to b[j] == True
            b[j] = False  # Mark position j as False

        i += 1  # Move to the next value
        j = (j + i) % n  # Update position j using modulo operation to wrap around

    # Step 5: Create a new list x containing only True values from b
    x = [a for a in b if a]  # List comprehension to filter True values from b

    # Step 6: Check if the list x is empty and print the result
    if len(x) == 0:  # Check if the length of x is 0
        print("YES")  # No True values left in b
    else:
        print("NO")  # There are still True values in b

# Entry point of the program
if __name__ == "__main__":
    process_values()  # Run the function to process values
