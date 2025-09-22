def main():
    # Receive input from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for the number of differences
    difference_count = 0

    # Compare corresponding elements of both lists
    for index in range(3):  # Loop through the first three elements
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1  # Increment the difference count

    # Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")  # Print "NO" otherwise

# Execute main function if script is run as the main program
if __name__ == "__main__":
    main()
