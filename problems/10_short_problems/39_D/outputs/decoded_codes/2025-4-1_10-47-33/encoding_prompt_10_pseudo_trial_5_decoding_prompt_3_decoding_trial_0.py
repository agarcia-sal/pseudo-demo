def do_main():
    # Initialize result counter
    res = 0

    # Prompt user for input
    print("Please enter the first line of numbers:")
    t1 = input()
    print("Please enter the second line of numbers:")
    t2 = input()

    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Iterate over each pair of numbers in the lists
    for index in range(3):
        # Convert string to integer
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Compare numbers and increment result counter if not equal
        if a != b:
            res += 1

    # Output result based on the count of mismatches
    if res < 3:
        print("YES")
    else:
        print("NO")

# Execute the function if the script is run as the main program
if __name__ == "__main__":
    do_main()
