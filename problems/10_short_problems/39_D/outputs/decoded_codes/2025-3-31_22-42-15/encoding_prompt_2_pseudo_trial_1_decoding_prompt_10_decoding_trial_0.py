def main():
    # Prompt the user for the first set of values and store in firstInput
    first_input = input()
    # Prompt the user for the second set of values and store in secondInput
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for the differences
    difference_count = 0
    
    # Compare the corresponding elements from both lists
    for index in range(3):  # We know there are exactly 3 values to compare
        first_value = int(first_values[index])   # Convert to integer
        second_value = int(second_values[index])  # Convert to integer
        
        # If the values are not equal, increment the difference count
        if first_value != second_value:
            difference_count += 1
            
    # After comparison, determine if fewer than 3 values are different
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
