def compare_input_values():
    # Prompt user to enter the first and second input strings
    first_input = input()
    second_input = input()
    
    # Split the input strings by spaces to create lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter variable for mismatches
    mismatch_count = 0
    
    # Loop to compare the first three elements of each list
    for index in range(3):
        # Convert the current values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Increment mismatch count if the values are not equal
        if first_value != second_value:
            mismatch_count += 1
            
    # Output result based on the number of mismatches
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Run the function if this script is executed as the main program
if __name__ == "__main__":
    compare_input_values()
