def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # If the current elements are not equal, increment the difference counter
        if first_value != second_value:
            difference_count += 1  # Increment if values are not equal
    
    # Check the number of differences
    if difference_count < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")   # Print "NO" otherwise

# Start the program
main()
