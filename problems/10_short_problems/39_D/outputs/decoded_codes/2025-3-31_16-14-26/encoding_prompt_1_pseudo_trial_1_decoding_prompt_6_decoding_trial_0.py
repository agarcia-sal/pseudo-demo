def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for mismatches
    mismatch_count = 0 
    
    # Loop through the first three values of both lists
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        # Convert the string values to integers for comparison
        value_a = int(first_values[index])  # Convert to integer
        value_b = int(second_values[index])  # Convert to integer
        
        # Check if the values are not equal
        if value_a != value_b:
            # Increment mismatch counter
            mismatch_count += 1 
    
    # Check the number of mismatches
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
main()
