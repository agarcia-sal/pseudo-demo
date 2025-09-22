def main():
    # Step 2: Get the size of the boolean list 'n' from the user
    n = int(input())
    
    # Step 3: Initialize a list 'boolean_list' with 'n' elements all set to TRUE
    boolean_list = [True] * n
    
    # Step 4: Set up index and increment variables
    index = 0
    increment = 1

    # Step 6: Mark elements in the boolean list
    while increment <= 500000:
        # Step 6a: Check if the current index is marked TRUE
        if boolean_list[index]:
            # Step 6a-i: Set the current index to FALSE
            boolean_list[index] = False
        
        # Step 6b: Increment
        increment += 1
        
        # Step 6c: Update index with wrap-around using modulo
        index = (index + increment) % n
    
    # Step 7: Create a new list of remaining TRUE values
    remaining_true = [value for value in boolean_list if value]
    
    # Step 8: Check if all values have been marked FALSE
    if len(remaining_true) == 0:
        print("YES")  # Step 8a: All values are FALSE
    else:
        print("NO")   # Step 9a: There are remaining TRUE values

# Ensure the script is run directly
if __name__ == "__main__":
    main()
