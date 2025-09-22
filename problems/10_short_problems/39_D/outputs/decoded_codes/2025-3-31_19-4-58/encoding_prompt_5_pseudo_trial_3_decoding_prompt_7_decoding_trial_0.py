def main():
    # Read input values from the user
    first_input = input()  # Get first set of numbers
    second_input = input()  # Get second set of numbers
    
    # Split the input strings into lists of values
    first_set = first_input.split()  # Convert the first input into a list
    second_set = second_input.split()  # Convert the second input into a list
    
    # Initialize a counter for differences
    difference_count = 0  # Counter for differences between sets

    # Compare the numerical values from both sets
    for index in range(3):  # Iterate over the indices 0 to 2
        # Convert the string values from both sets to integers
        first_value = int(first_set[index])  # Convert first set value
        second_value = int(second_set[index])  # Convert second set value
        
        # Check if the values are different
        if first_value != second_value:  # If they are not equal
            difference_count += 1  # Increment the difference counter

    # Determine if the number of differences is less than 3
    if difference_count < 3:  # If differences are fewer than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO for three or more differences

# Program execution starts here
main()
