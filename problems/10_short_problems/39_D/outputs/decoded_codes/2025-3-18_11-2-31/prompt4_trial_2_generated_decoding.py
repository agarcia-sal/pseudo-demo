def do_main():
    # Read two lines of input from the user
    input1 = input()
    input2 = input()

    # Split the input strings into lists of strings
    list1 = input1.split()
    list2 = input2.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding string elements to integers
        a = int(list1[index])
        b = int(list2[index])

        # Check if the values are different
        if a != b:
            # Increment the difference counter
            difference_count += 1

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Start the program by executing the main function
if __name__ == "__main__":
    do_main()
