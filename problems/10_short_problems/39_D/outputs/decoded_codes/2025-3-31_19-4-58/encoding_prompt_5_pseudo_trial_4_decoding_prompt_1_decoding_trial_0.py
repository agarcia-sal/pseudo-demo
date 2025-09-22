def main():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of strings
    listFirst = firstLine.split()
    listSecond = secondLine.split()
    
    # Initialize a counter to keep track of differences
    differenceCount = 0 

    # Loop through each of the three numbers
    for index in range(3):
        # Convert the string numbers into integers
        numberFromFirstList = int(listFirst[index])
        numberFromSecondList = int(listSecond[index])
        
        # Check if the numbers are different
        if numberFromFirstList != numberFromSecondList:
            # Increment the difference counter
            differenceCount += 1 

    # Determine the result based on the number of differences
    if differenceCount < 3:
        # If there are less than 3 differences, print "YES"
        print("YES")
    else:
        # If there are 3 or more differences, print "NO"
        print("NO")

# Call the main function to execute the program
main()
