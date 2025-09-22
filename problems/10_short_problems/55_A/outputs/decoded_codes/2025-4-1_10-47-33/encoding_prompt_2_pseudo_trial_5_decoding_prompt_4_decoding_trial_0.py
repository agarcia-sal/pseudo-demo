def main():
    # Step 1: Get the total number of elements from the user
    total_elements = int(input())

    # Step 3: Initialize a list of booleans set to True
    boolean_list = [True] * total_elements
    
    # Step 4: Initialize the current index and increment
    current_index = 0
    increment = 1

    # Step 5: Loop until increment exceeds 500,000
    while increment <= 500000:
        # Step 5a: Check if the current index position is True
        if boolean_list[current_index]:
            # Step 5a.i: Set the position to False
            boolean_list[current_index] = False
        
        # Step 5b: Increase the increment
        increment += 1
        
        # Step 5c: Update the current index
        current_index = (current_index + increment) % total_elements

    # Step 6: Create a list of remaining True values
    remaining_true_values = [value for value in boolean_list if value]

    # Step 7: Check the length of the remaining true values
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Step 8: Call the main function to execute the program
if __name__ == "__main__":
    main()
