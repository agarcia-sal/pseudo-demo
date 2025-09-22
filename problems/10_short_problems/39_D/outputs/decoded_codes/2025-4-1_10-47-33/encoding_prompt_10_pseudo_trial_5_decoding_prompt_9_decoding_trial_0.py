def doMain():
    # Initialize variables
    t1 = ""  # First line of numbers as a string
    t2 = ""  # Second line of numbers as a string
    res = 0  # Counter for differences

    # Read inputs from the user
    print("Please enter the first line of numbers:")
    t1 = input()
    print("Please enter the second line of numbers:")
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()  # First line split into list
    tt2 = t2.split()  # Second line split into list

    # Loop through the expected range (0 to 2)
    for index in range(3):
        a = int(tt1[index])  # Convert first line string to integer
        b = int(tt2[index])  # Convert second line string to integer
        
        # Increment counter if the numbers are not equal
        if a != b:
            res += 1

    # Output based on the count of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Ensure the script executes the function if run as the main program
if __name__ == "__main__":
    doMain()
