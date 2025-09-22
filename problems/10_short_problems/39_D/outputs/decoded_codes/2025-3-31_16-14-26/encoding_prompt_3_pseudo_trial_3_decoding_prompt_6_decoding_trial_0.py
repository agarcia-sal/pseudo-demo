def main():
    # Step 1: Read input from the user
    user_input1 = input()  # First input from the user
    user_input2 = input()  # Second input from the user
    
    # Step 2: Split the inputs into lists of strings
    input_list1 = user_input1.split()  # List of strings from the first input
    input_list2 = user_input2.split()  # List of strings from the second input
    
    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter for the differences
    
    # Step 4: Compare the elements of the two lists
    for index in range(3):  # Loop through the first three elements
        # Convert string elements to integers for comparison
        number1 = int(input_list1[index])  # Convert the current element of first list to integer
        number2 = int(input_list2[index])  # Convert the current element of second list to integer
        
        # Step 5: Check if the numbers are different
        if number1 != number2:  # If the numbers are not equal
            difference_count += 1  # Increment the difference counter
    
    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:  # If there are fewer than 3 differences
        print("YES")  # Output "YES"
    else: 
        print("NO")  # Output "NO"

# Step 7: Execute the main function when the program is run
if __name__ == "__main__":
    main()  # Call the main function
