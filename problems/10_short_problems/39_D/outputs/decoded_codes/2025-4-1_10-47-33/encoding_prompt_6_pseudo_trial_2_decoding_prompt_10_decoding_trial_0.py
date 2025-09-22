def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into separate values
    first_values = first_line.split()
    second_values = second_line.split()
    
    # Initialize a variable to count differences
    difference_count = 0 
    
    # Compare corresponding values from both lists
    for index in range(3):  # Loop through the first three elements
        # Convert values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check for inequality between the two values
        if first_value != second_value:
            difference_count += 1  # Increase the difference count if not equal

    # Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main function
main()


1 2 3
1 2 4


YES


5 6 7
8 9 10


NO


1 1 1
1 1 1


YES
