def compare_three_integers():
    # Prompt user for input and store as firstInput
    first_input = input()
    # Prompt user for input and store as secondInput
    second_input = input()
    
    # Split firstInput into a list of strings
    first_list = first_input.split()
    # Split secondInput into a list of strings
    second_list = second_input.split()
    
    # Initialize the difference counter
    difference_count = 0

    # Comparison loop for the first three integers
    for index in range(3):
        # Convert items in lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Increment difference count if the values are not equal
        if first_value != second_value:
            difference_count += 1
    
    # Check the condition and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the function to run the program
compare_three_integers()
