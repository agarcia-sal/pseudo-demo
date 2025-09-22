def compare_input_values():
    # Prompt user to enter the first input string
    first_input = input()
    # Prompt user to enter the second input string
    second_input = input()
    
    # Split input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for mismatches
    mismatch_count = 0
    
    # Compare the values in both lists
    for index in range(3):
        # Convert string values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Increment the mismatch count if values differ
        if first_value != second_value:
            mismatch_count += 1
            
    # Output result based on the number of mismatches
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function if this script is run as the main program
if __name__ == "__main__":
    compare_input_values()
