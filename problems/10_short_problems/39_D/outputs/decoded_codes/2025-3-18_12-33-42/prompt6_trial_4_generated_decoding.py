def do_main():
    # Read two separate lines of input from the user
    first_line = input()
    second_line = input()

    # Split the input strings into lists of numbers
    first_list = first_line.split()
    second_list = second_line.split()

    # Initialize a counter for the number of differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from string to integer
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # If there are less than 3 differences, output "YES"; otherwise, output "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
do_main()
