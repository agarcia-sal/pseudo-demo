def main():
    # Step 2: Get a number 'n' from the user which indicates the size of the list.
    n = int(input())
    
    # Step 3: Initialize a list 'booleanList' with 'n' elements all set to TRUE.
    boolean_list = [True] * n
    
    index = 0  # Step 4: Initialize index to 0
    increment = 1  # Step 5: Initialize increment to 1
    
    # Step 6: WHILE increment is less than or equal to 500000
    while increment <= 500000:
        # Step 6a: If current index is still marked as True
        if boolean_list[index]:
            boolean_list[index] = False  # Step 6ai: Mark it as FALSE
        
        increment += 1  # Step 6b: Increase increment by 1
        index = (index + increment) % n  # Step 6c: Update index with modulo wrapping
    
    # Step 7: Create a list of remaining True values
    remaining_true = [value for value in boolean_list if value]
    
    # Step 8: Check if any TRUE values remain
    if len(remaining_true) == 0:
        print("YES")  # All values have been marked FALSE
    else:
        print("NO")   # There are still some TRUE values
    
# Step 10: Run the main function to execute the program
if __name__ == "__main__":
    main()
