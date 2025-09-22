def main():
    # Read input values
    t1 = input()
    t2 = input()

    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize the result counter
    differenceCount = 0 

    # Compare the first three elements of both lists
    for index in range(3):
        a = int(tt1[index])
        b = int(tt2[index])
        if a != b:
            differenceCount += 1

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script runs
main()
