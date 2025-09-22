def compare_input_values():
    # Prompt the user for input and store the first and second input strings
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize the mismatch counter
    mismatch_count = 0
    
    # Iterate through the indices of the first three values
    for index in range(3):
        # Convert values to integers for comparison
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Increment mismatch count if values are not equal
        if first_value != second_value:
            mismatch_count += 1
    
    # Output "YES" if there are fewer than three mismatches, otherwise "NO"
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the function if the script is run as the main program
if __name__ == "__main__":
    compare_input_values()
