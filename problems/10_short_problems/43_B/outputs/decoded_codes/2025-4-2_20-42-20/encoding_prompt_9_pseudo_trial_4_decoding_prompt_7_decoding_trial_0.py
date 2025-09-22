# Step 1: Receive Input
first_string = input()
second_string = input()

# Step 2: Process Input
# Remove all spaces from both strings
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Step 3: Initialize Frequency Count
# We will use a dictionary to count character frequencies
character_frequencies = {}

# Step 4: Count Character Frequencies
# Function to count characters in a string
def count_characters(string):
    freq = {}
    for character in string:  # Iterate through each character in the string
        if character in freq:
            freq[character] += 1  # Increment count for existing character
        else:
            freq[character] = 1  # Initialize count for new character
    return freq

# Count frequencies for both strings
first_freq = count_characters(cleaned_first_string)
second_freq = count_characters(cleaned_second_string)

# Fill character_frequencies with differences
for character in range(ord('A'), ord('z') + 1):  # From 'A' to 'z'
    char = chr(character)
    count_first = first_freq.get(char, 0)  # Get frequency or 0 if not present
    count_second = second_freq.get(char, 0)  # Get frequency or 0 if not present
    character_frequencies[char] = count_first - count_second  # Store difference

# Step 5: Evaluate Frequencies
has_shortages = 'NO'  # Initialize as no shortages found
for freq in character_frequencies.values():
    if freq < 0:  # If there's any negative value
        has_shortages = 'YES'  # Shortage detected
        break  # No need to check further

# Step 6: Output Result
if has_shortages == 'NO':
    print("YES")  # First string can form second string
else:
    print("NO")  # Shortage exists
