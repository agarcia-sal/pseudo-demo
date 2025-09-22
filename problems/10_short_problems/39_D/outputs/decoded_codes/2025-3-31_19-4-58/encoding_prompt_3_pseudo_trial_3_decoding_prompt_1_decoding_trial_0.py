def main_function():
    # Get two lines of input from the user
    first_line = input()
    second_line = input()

    # Split the input lines into separate elements
    first_array = first_line.split()
    second_array = second_line.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both arrays
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_array[index])
        second_value = int(second_array[index])
        
        # Compare the two values
        if first_value != second_value:
            # Increment the difference counter if they do not match
            difference_count += 1

    # Check if the count of differences is less than 3
    if difference_count < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# This function is invoked to run the main logic
if __name__ == "__main__":
    main_function()
