def do_main():
    # Input: Two strings representing sequences of numbers
    t1 = input()
    t2 = input()

    # Split the input strings into lists of substrings
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize result counter
    res = 0

    # Loop through the first three elements of tt1 and tt2
    for index in range(3):
        # Parse the string elements as integers
        a = int(tt1[index])
        b = int(tt2[index])

        # Compare the two integers a and b
        if a != b:
            # Increment the result counter if the values are different
            res += 1

    # Check the result counter
    if res < 3:
        # If less than 3 differences, print "YES"
        print("YES")
    else:
        # If 3 or more differences, print "NO"
        print("NO")

# Execute the main function if this is the main module
if __name__ == "__main__":
    do_main()
