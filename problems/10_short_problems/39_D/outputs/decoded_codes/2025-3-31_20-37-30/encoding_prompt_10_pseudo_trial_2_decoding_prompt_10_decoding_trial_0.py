def do_main():
    # Obtain two strings from user input
    string1 = input()
    string2 = input()

    # Split the strings into lists of elements
    list1 = string1.split()
    list2 = string2.split()

    # Initialize a variable to count the differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements to integers
        value_a = int(list1[index])
        value_b = int(list2[index])
        
        # Check if the values are different
        if value_a != value_b:
            # Increment the difference count
            difference_count += 1

    # Determine if fewer than 3 differences are found
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Execute main function if this is the entry point of the program
if __name__ == "__main__":
    do_main()
