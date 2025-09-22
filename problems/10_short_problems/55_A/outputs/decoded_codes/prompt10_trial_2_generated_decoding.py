def main():
    # Step 1: Input the size of the array
    n = int(input())
    
    # Step 2: Initialize the boolean array
    boolean_array = [True] * n  # Create and fill with True
    
    # Step 3: Initialize variables for iteration
    j = 0
    i = 1
    
    # Step 4: Iterate while i is less than or equal to 500000
    while i <= 500000:
        # Step 5: Check and modify the boolean array
        if boolean_array[j]:
            boolean_array[j] = False  # Mark the boolean array's index as inactive
        
        # Step 6: Increment i and update j
        i += 1
        j = (j + i) % n  # Ensure j wraps around using modulo
    
    # Step 7: Create a new list containing TRUE values from boolean_array
    true_values = [value for value in boolean_array if value]  # Filter for True values
    
    # Step 8: Check if the list of true values is empty
    if not true_values:
        print('YES')  # Output 'YES' if there are no True values
    else:
        print('NO')   # Output 'NO' if there are True values

if __name__ == "__main__":
    main()
