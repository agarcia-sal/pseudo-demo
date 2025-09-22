def main():
    # Read input strings representing a series of values
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_values = first_input.split()
    second_values = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers for comparison
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Compare the current elements from both lists
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1 

    # Check if the count of differences is less than 3
    if difference_count < 3:
        # Print "YES" if there are less than 3 differences
        print("YES")
    else:
        # Print "NO" if there are 3 or more differences
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
