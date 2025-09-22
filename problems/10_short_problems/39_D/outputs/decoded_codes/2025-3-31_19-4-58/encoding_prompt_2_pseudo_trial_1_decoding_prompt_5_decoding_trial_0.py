def main():
    # Get user inputs for comparison
    first_input = input()
    second_input = input()
    
    # Split inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a mismatch counter
    mismatch_count = 0
    
    # Compare values in the lists
    for index in range(3):  # We compare the first three elements
        first_value = int(first_list[index])   # Convert first list value to integer
        second_value = int(second_list[index])  # Convert second list value to integer
        
        # Increment mismatch count if values are not equal
        if first_value != second_value:
            mismatch_count += 1
    
    # Check mismatch count and output the result
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
