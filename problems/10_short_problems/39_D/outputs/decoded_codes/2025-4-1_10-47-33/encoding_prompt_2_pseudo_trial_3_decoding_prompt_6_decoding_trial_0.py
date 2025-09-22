def main():
    # Prompt for user input
    first_input = input()  # Read the first line of input
    second_input = input()  # Read the second line of input

    # Split the input strings into lists
    first_list = first_input.split()  # Create a list from the first input
    second_list = second_input.split()  # Create a list from the second input

    # Initialize a counter for differences
    difference_count = 0  # Start with a count of zero

    # Compare elements of both lists
    for index in range(3):  # Loop through the first 3 elements
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1  # Increment the difference count

    # Decide the result based on the count of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Execute the main function if the file is run as a script
if __name__ == "__main__":
    main()
