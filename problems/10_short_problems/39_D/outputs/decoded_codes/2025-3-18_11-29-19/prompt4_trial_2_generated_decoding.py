def do_main():
    # Read two lines of input
    input1 = input()
    input2 = input()

    # Split input lines into lists of strings
    list1 = input1.split()
    list2 = input2.split()

    # Initialize a counter for differences
    difference_count = 0

    # Compare each element of the two lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        value1 = int(list1[index])
        value2 = int(list2[index])

        # If elements are not equal, increment the counter
        if value1 != value2:
            difference_count += 1

    # If differences are less than 3, print "YES", else print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starting point
if __name__ == "__main__":
    do_main()
