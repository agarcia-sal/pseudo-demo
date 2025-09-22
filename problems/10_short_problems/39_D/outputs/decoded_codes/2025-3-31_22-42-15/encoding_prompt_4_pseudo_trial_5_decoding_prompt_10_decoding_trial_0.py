def do_main():
    # Read input strings
    t1 = input()
    t2 = input()

    # Split the input strings into lists of values
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Iterate over the first three elements of both lists
    for index in range(3):
        value_a = int(tt1[index])
        value_b = int(tt2[index])

        # Check if the values are different
        if value_a != value_b:
            difference_count += 1

    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution
do_main()
