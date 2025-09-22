def can_construct_string():
    # Input Strings
    firstString = input()
    secondString = input()

    # Process Input
    firstString = firstString.replace(' ', '')
    secondString = secondString.replace(' ', '')

    # Initialize Frequency Count
    characterDifferences = [0] * (ord('z') - ord('A') + 1)

    # Maximum ASCII range from 'A' to 'z'
    for char in range(ord('A'), ord('z') + 1):
        count_first = firstString.count(chr(char))
        count_second = secondString.count(chr(char))
        characterDifferences[char - ord('A')] = count_first - count_second

    # Check Feasibility
    if all(count >= 0 for count in characterDifferences):
        print("YES")
    else:
        print("NO")

# Run the function
can_construct_string()


from collections import Counter

def can_construct_string():
    # Input Strings
    firstString = input()
    secondString = input()

    # Process Input
    firstString = firstString.replace(' ', '')
    secondString = secondString.replace(' ', '')

    # Count characters
    count_first = Counter(firstString)
    count_second = Counter(secondString)

    # Check Feasibility
    for char, count in count_second.items():
        if count_first[char] < count:
            print("NO")
            return

    print("YES")

# Run the function
can_construct_string()
