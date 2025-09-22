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
    for index in range(3):
        # Convert the current elements to integers
        value_a = int(first_list[index])
        value_b = int(second_list[index])
        
        # Check if the elements are different
        if value_a != value_b:
            # Increment the difference counter
            difference_count += 1

    # After checking all elements, determine the output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function
main()
