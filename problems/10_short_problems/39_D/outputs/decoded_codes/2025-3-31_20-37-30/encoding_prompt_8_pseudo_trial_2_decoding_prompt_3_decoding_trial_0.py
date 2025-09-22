def main():
    # Step 1: Get two strings of numbers from the user
    inputString1 = input()
    inputString2 = input()

    # Step 2: Split the input strings into individual numbers
    numbersList1 = inputString1.split()
    numbersList2 = inputString2.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare each corresponding number in the two lists
    for index in range(3):
        number1 = int(numbersList1[index])
        number2 = int(numbersList2[index])

        # Step 5: Check if the numbers are different
        if number1 != number2:
            differenceCount += 1

    # Step 6: Determine if the count of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Trigger the main function if the script is run directly
if __name__ == "__main__":
    main()
