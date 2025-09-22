def doMain():
    # Initialization of variables
    t1 = ""
    t2 = ""
    res = 0

    # Input for two lines of numbers
    print("Please enter the first line of numbers:")
    t1 = input()
    print("Please enter the second line of numbers:")
    t2 = input()

    # Splitting the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Loop through the indices of the lists
    for index in range(3):  # Since we know we will have exactly three numbers
        # Convert the string numbers to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Check if the two numbers are not equal
        if a != b:
            res += 1  # Increment the result counter if they are not equal

    # Output based on the value of res
    if res < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the script
if __name__ == "__main__":
    doMain()
