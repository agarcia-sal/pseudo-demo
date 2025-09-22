def main():
    # Prompt user for input and store in variable first_input
    first_input = input()
    # Prompt user for input and store in variable second_input
    second_input = input()

    # Split input strings into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for the differences
    difference_count = 0

    # Compare the elements of both lists
    for index in range(3):  # Loop through the first three elements
        # Convert string elements to integers for comparison
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])

        # Check if the values are different
        if value_from_first_list != value_from_second_list:  
            # Increment the difference count if values are different
            difference_count += 1

    # Evaluate how many differences were found
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Print "YES"
    else:
        print("NO")  # Otherwise, print "NO"

# Execute the main function
main()
