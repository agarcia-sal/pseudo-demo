# Start Program

def do_main():
    # Receive First Input
    first_input = input()  # Store the first line of input
    
    # Receive Second Input
    second_input = input()  # Store the second line of input
    
    # Split Inputs into Lists
    first_list = first_input.split()  # Create a list by splitting the first input
    second_list = second_input.split()  # Create a list by splitting the second input

    # Initialize a Counter for Differences
    difference_count = 0  # Set a variable to count differences

    # Loop through the Range from 0 to 2 (for three comparisons)
    for i in range(3):
        # Convert the elements to integers
        value_from_first = int(first_list[i])  # Get integer from first list
        value_from_second = int(second_list[i])  # Get integer from second list
        
        # If the two values are not equal
        if value_from_first != value_from_second:
            difference_count += 1  # Increment differences

    # Check the Number of Differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the Function do_main when the Program Starts
do_main()

# End Program
