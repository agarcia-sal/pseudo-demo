def doMain():
    # Read two strings from user input
    string1 = input()
    string2 = input()

    # Split input strings into lists of substrings
    list1 = string1.split()
    list2 = string2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the first three elements of both lists
    for index in range(3):  # Range from 0 to 2
        # Convert list elements to integers for comparison
        value_from_list1 = int(list1[index])        # Integer conversion of list1[index]
        value_from_list2 = int(list2[index])        # Integer conversion of list2[index]

        # Check if the values are different
        if value_from_list1 != value_from_list2:     # Checking for inequality
            difference_count += 1                     # Increment counter if values are different

    # Determine if less than three differences were found
    if difference_count < 3:                         # Check if the count of differences is less than 3
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    doMain()
