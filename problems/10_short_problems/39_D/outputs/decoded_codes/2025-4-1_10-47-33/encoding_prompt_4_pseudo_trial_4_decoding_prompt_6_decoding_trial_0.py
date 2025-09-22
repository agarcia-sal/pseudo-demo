# Define the main function
def do_main():
    # Read two lines of input
    first_line = input()  # Input for the first list of numbers
    second_line = input()  # Input for the second list of numbers

    # Split input lines into lists of strings
    list1 = first_line.split()  # Split the first line
    list2 = second_line.split()  # Split the second line

    # Initialize a counter for differences
    difference_count = 0  # Counter starts at 0

    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2 inclusive
        # Convert the string elements to integers
        value_a = int(list1[index])  # Integer value from the first list
        value_b = int(list2[index])  # Integer value from the second list

        # Check if the two values are different
        if value_a != value_b:  # Compare the values
            difference_count += 1  # Increment counter for differences

    # Check the number of differences
    if difference_count < 3:  # If less than 3 differences
        print("YES")  # Output YES
    else:  # If 3 or more differences
        print("NO")  # Output NO

# Main program execution
if __name__ == "__main__":  # Check if this is the main module
    do_main()  # Call the main function
