def main():
    # Read the value of n
    n = int(input())
    
    # Create an array b of size n and initialize all elements to True
    b = [True] * n
    
    # Initialize variables
    j = 0  # This will be our index in the array
    i = 1  # This is our counter

    # Loop until i exceeds 500000
    while i <= 500000:
        if b[j]:
            b[j] = False  # Mark the current position as False
        i += 1  # Increment the counter
        j = (j + i) % n  # Update index j based on current i

    # Collect all True values from the array b
    remaining_true = [value for value in b if value]

    # Check if there are any True values left
    if len(remaining_true) == 0:
        print('YES')  # All positions marked False
    else:
        print('NO')   # There are still some True positions left

# Start the program
if __name__ == "__main__":
    main()
