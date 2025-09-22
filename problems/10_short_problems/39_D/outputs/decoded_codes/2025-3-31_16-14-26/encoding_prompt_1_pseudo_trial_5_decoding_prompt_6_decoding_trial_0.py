def main():
    # Read two lines of input, representing two sets of values
    first_input = input()  # Read the first input line
    second_input = input()  # Read the second input line
    
    # Split the input strings into lists of values
    first_values = first_input.split()  # Split first input into list
    second_values = second_input.split()  # Split second input into list
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop for the first three elements
        # Convert the string values to integers for comparison
        value_from_first = int(first_values[index])  # Convert to integer
        value_from_second = int(second_values[index])  # Convert to integer
        
        # Check if the values are different
        if value_from_first != value_from_second:  # Compare values
            # Increment the difference counter
            difference_count += 1  # Increase count if values differ
            
    # Check the number of differences and print the result
    if difference_count < 3:  # If diffs are less than 3
        print("YES")  # Print YES if conditions are met
    else:
        print("NO")  # Otherwise print NO

# Start the program execution
main()
