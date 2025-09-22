def do_main():
    # Read two lines of input
    input_line1 = input()
    input_line2 = input()

    # Split the input lines into lists of strings
    list1 = input_line1.split()
    list2 = input_line2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare elements of both lists
    for index in range(3):
        value1 = int(list1[index])
        value2 = int(list2[index])

        # Increment the difference count if values are not equal
        if value1 != value2:
            difference_count += 1 

    # Check the number of differences and print result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    do_main()
