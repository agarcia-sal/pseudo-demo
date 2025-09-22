def check_character_frequencies():
    # Step 1: Accept two lines of input from the user
    first_string = input()
    second_string = input()

    # Step 2: Prepare the strings by removing spaces
    s1 = first_string.replace(" ", "")
    s2 = second_string.replace(" ", "")

    # Step 3: Initialize a frequency list to count character differences
    # 256 is chosen to cover all ASCII characters
    frequencies = [0] * 256

    # Step 4: Calculate character frequency differences
    for char in range(ord('A'), ord('z') + 1):
        count_in_s1 = s1.count(chr(char))
        count_in_s2 = s2.count(chr(char))
        difference = count_in_s1 - count_in_s2
        frequencies[char] += difference

    # Step 5: Check for any negative frequencies
    has_negative = False
    for frequency in frequencies:
        if frequency < 0:
            has_negative = True
            break

    # Step 6: Produce the output based on the presence of negative frequencies
    if not has_negative:
        print("YES")
    else:
        print("NO")

# Sample test cases which can be uncommented to test the function
# check_character_frequencies()  # Input: "A quick brown fox", "A brown quick fox"
# check_character_frequencies()  # Input: "Hello, World!", "World, Hello!"
