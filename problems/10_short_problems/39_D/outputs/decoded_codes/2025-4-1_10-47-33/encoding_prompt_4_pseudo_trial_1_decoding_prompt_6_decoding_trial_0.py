def main():
    # Read input values
    user_input_1 = input()  # Input for the first set of values
    user_input_2 = input()  # Input for the second set of values

    # Split the input strings into lists
    list1 = user_input_1.split()  # Split first input into words
    list2 = user_input_2.split()  # Split second input into words

    # Initialize difference counter
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):  # Range from 0 to 2 (inclusive)
        # Convert string values to integers
        value1 = int(list1[index])  # Convert first list element to integer
        value2 = int(list2[index])  # Convert second list element to integer
        
        # Count differences
        if value1 != value2:  # Check if values are not equal
            difference_count += 1  # Increment difference counter

    # Determine output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Execute main function
main()
