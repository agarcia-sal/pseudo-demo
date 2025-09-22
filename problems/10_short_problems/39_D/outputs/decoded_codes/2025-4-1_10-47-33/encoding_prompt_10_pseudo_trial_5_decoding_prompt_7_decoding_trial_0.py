def doMain():
    # Initialize a response counter
    res = 0

    # Asking for user input
    print("Please enter the first line of numbers:")
    t1 = input()
    print("Please enter the second line of numbers:")
    t2 = input()

    # Splitting the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Iterate through the first three indexes of the lists
    for index in range(3):
        # Convert string numbers to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Increment response counter if the numbers do not match
        if a != b:
            res += 1

    # Determine the output based on the count of mismatches
    if res < 3:
        print("YES")
    else:
        print("NO")

# Check if the script is being run as the main program
if __name__ == "__main__":
    doMain()
