def main():
    # Step 2: Get the size of the list from the user
    n = int(input())
    
    # Step 3: Initialize a boolean list with all elements set to TRUE (True in Python)
    boolean_list = [True] * n
    
    index = 0  # Step 4: Set the initial index
    increment = 1  # Step 5: Set the initial increment

    # Step 6: Start the marking process
    while increment <= 500000:
        # Step 6a: If the current position is TRUE
        if boolean_list[index]:
            boolean_list[index] = False  # Mark it as FALSE
        
        increment += 1  # Step 6b: Increase increment by 1
        index = (index + increment) % n  # Step 6c: Update index with wrap-around
    
    # Step 7: Create a list of remaining TRUE values
    remaining_true = [value for value in boolean_list if value]
    
    # Step 8: Check if any TRUE values remain and print result
    if len(remaining_true) == 0:
        print("YES")  # Step 8a
    else:
        print("NO")  # Step 9a

# To run the main function
if __name__ == "__main__":
    main()
