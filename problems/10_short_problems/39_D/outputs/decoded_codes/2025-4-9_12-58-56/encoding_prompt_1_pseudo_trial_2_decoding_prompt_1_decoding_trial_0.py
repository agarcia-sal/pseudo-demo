def main():
    # Read two lines of input from the user
    firstSetOfNumbers = input()
    secondSetOfNumbers = input()

    # Split the input lines into individual numbers
    firstNumbers = firstSetOfNumbers.split()
    secondNumbers = secondSetOfNumbers.split()
    
    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the first three numbers from both lists
    for index in range(3):
        # Convert the current numbers to integers
        numberFromFirstSet = int(firstNumbers[index])
        numberFromSecondSet = int(secondNumbers[index])
        
        # Check if the numbers are different
        if numberFromFirstSet != numberFromSecondSet:
            differenceCount += 1 

    # Check the total number of differences
    if differenceCount < 3:
        print("YES")
    else: 
        print("NO")

# Start the program by calling the main function
main()
