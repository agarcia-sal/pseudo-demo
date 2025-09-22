def main_function():
    # Read two input strings
    first_string = input()
    second_string = input()

    # Split the input strings into lists of substrings
    first_list = first_string.split()
    second_list = second_string.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements from strings to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values at the current index are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main_function()


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     1 5 3
     

     1 2 3
     4 5 6
     

     1 2 3
     1 2 3 7
     