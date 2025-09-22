def main():
    # Read two lines of input
    firstString = input()
    secondString = input()

    # Split the input strings into lists of words
    list1 = firstString.split()
    list2 = secondString.split()

    # Initialize a counter for differences
    differencesCount = 0 

    # Iterate over the first three elements of both lists
    for index in range(3):  # range(3) generates numbers 0, 1, 2
        # Convert the elements to integers
        integer1 = int(list1[index])
        integer2 = int(list2[index])

        # Check if the integers are different
        if integer1 != integer2:
            # Increment the differences counter
            differencesCount += 1 

    # Check if the number of differences is less than 3
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main()
