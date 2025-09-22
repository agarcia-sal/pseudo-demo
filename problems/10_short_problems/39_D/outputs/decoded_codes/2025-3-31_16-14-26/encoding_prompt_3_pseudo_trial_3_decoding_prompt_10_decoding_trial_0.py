def main():
    # Step 1: Read input from the user
    user_input_1 = input()
    user_input_2 = input()
    
    # Step 2: Split the inputs into lists of strings
    input_list_1 = user_input_1.split()
    input_list_2 = user_input_2.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare the elements of the two lists
    for index in range(3):  # We assume inputs will have at least 3 elements
        # Convert string elements to integers for comparison
        number1 = int(input_list_1[index])
        number2 = int(input_list_2[index])
        
        # Step 5: Check if the numbers are different
        if number1 != number2:
            # Increment the difference counter
            difference_count += 1
    
    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function when the program is run
if __name__ == "__main__":
    main()
