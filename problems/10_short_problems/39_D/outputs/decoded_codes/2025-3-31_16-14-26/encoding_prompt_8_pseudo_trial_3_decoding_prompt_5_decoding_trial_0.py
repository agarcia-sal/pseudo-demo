def main():
    # Read the first set of three integers from user input
    first_input_line = input()
    # Read the second set of three integers from user input
    second_input_line = input()

    # Split the input lines into lists of strings
    first_set = first_input_line.split()
    second_set = second_input_line.split()

    # Initialize a counter to track the number of mismatches
    mismatch_count = 0 

    # Iterate through each index from 0 to 2 (for three comparisons)
    for index in range(3):
        # Convert the string values to integers for comparison
        first_value = int(first_set[index])
        second_value = int(second_set[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the mismatch counter
            mismatch_count += 1 

    # Check if the number of mismatches is less than 3
    if mismatch_count < 3:
        # If there are fewer than 3 mismatches, print "YES"
        print("YES")
    else:
        # If there are 3 or more mismatches, print "NO"
        print("NO")

# Start execution of the program by calling the main function
main()
