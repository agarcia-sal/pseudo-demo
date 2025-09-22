def main():
    # Read input values
    first_input = input()
    second_input = input()
    
    # Split input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a mismatch counter
    mismatch_count = 0 
    
    # Compare each corresponding value in the two lists
    for index in range(3):
        # Convert string values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check for mismatch
        if first_value != second_value:
            mismatch_count += 1
    
    # Determine if the number of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
