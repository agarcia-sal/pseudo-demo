def do_main():
    # Read input values for two sequences
    first_sequence = input()
    second_sequence = input()
    
    # Split the input strings into lists of string representations of numbers
    first_list = first_sequence.split()
    second_list = second_sequence.split()
    
    # Initialize a counter for mismatches
    mismatch_count = 0 
    
    # Iterate over the indices of the first three elements (or the length of the shorter list)
    for index in range(min(3, len(first_list), len(second_list))):
        # Convert the corresponding elements in both lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the mismatch counter
            mismatch_count += 1
    
    # Determine if the count of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution point
if __name__ == "__main__":
    do_main()
