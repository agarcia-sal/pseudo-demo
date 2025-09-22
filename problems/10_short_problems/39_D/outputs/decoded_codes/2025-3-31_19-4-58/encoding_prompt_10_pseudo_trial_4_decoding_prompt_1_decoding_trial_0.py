def doMain():
    t1 = ""  # Declare variable as string
    t2 = ""  # Declare variable as string
    tt1 = []  # Declare variable as list of strings
    tt2 = []  # Declare variable as list of strings
    res = 0   # Declare variable as integer with initial value 0

    # Read two lines of input from the user
    t1 = input()
    t2 = input()

    # Split the input strings into lists of substrings
    tt1 = t1.split()  # Split t1 using space as delimiter
    tt2 = t2.split()  # Split t2 using space as delimiter

    # Iterate over the first three elements of both lists
    for index in range(3):  # From 0 to 2
        a = int(tt1[index])  # Convert tt1[index] to integer
        b = int(tt2[index])  # Convert tt2[index] to integer

        # Check if the values are different
        if a != b:  # If a is not equal to b
            res += 1  # Increment res by 1

    # Determine if the number of differences is less than three
    if res < 3:  # If res is less than 3
        print("YES")
    else:
        print("NO")

# Main execution block
doMain()
