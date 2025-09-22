def do_main():
    # Read two lines of input
    first_line = input()
    second_line = input()

    # Split input lines into lists of strings
    list1 = first_line.split()
    list2 = second_line.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        value_a = int(list1[index])
        value_b = int(list2[index])

        # Check if the two values are different
        if value_a != value_b:
            difference_count += 1

    # Check the number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Main program execution
if __name__ == "__main__":
    do_main()
