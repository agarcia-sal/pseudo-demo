def main():
    # Step 1: Read the value of n
    n = int(input())
    
    # Step 2: Initialize an array b of size n, with all elements set to True
    b = [True] * n
    
    # Initialize index j and counter i
    j = 0
    i = 1

    # Step 3: Loop until i exceeds 500000
    while i <= 500000:
        if b[j]:
            # Mark the current position as False
            b[j] = False
        
        # Increment i by 1
        i += 1
        
        # Update index j based on current i
        j = (j + i) % n

    # Step 4: Collect all True values from array b
    true_positions = [value for value in b if value]

    # Step 5: Check if there are any True values left in true_positions
    if len(true_positions) == 0:
        print('YES')  # All positions marked False
    else:
        print('NO')   # There are still some True positions left

# Start the program
if __name__ == "__main__":
    main()
