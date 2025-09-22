def main():
    # Step 1: Read input from the user
    user_input1 = input()  # User's first input
    user_input2 = input()  # User's second input
    
    # Step 2: Split the inputs into lists of strings
    input_list1 = user_input1.split()  # Split first input into list of strings
    input_list2 = user_input2.split()  # Split second input into list of strings
    
    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter for the number of differences
    
    # Step 4: Compare the elements of the two lists
    for index in range(3):  # Assuming both lists contain at least 3 elements
        # Convert string elements to integers for comparison
        number1 = int(input_list1[index])  # Convert and store the first number
        number2 = int(input_list2[index])  # Convert and store the second number
        
        # Step 5: Check if the numbers are different
        if number1 != number2:  # If the numbers are not the same
            # Increment the difference counter
            difference_count += 1  # Increase the count of differences

    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:  # Check if differences are less than 3
        print("YES")  # Print YES if true
    else:
        print("NO")  # Print NO if false

# Step 7: Execute the main function when the program is run
if __name__ == "__main__":
    main()  # Call the main function
