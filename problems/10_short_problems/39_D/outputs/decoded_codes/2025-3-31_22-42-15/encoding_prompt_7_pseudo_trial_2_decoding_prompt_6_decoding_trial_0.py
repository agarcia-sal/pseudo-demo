def compare_input_values():
    # Prompt user to enter the first input string
    first_input = input()
    # Prompt user to enter the second input string
    second_input = input()
    
    # Split input strings by spaces into lists
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize mismatch counter
    mismatch_count = 0
    
    # Loop through the first three indices
    for index in range(3):
        # Convert the values from string to integer
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are not equal
        if first_value != second_value:
            mismatch_count += 1
    
    # Output "YES" if mismatches are less than 3, else "NO"
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function if this script is the main program
if __name__ == "__main__":
    compare_input_values()
