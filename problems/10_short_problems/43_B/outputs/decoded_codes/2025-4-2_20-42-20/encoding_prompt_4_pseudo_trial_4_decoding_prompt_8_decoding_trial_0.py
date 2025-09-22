def check_character_frequency_difference():
    s1 = []
    s2 = []

    for i in range(2):
        input_string = input()
        cleaned_string = input_string.replace(" ", "")
        if i == 0:
            s1.append(cleaned_string)
        else:
            s2.append(cleaned_string)

    freqs = []
    
    for char in range(ord('A'), ord('z') + 1):
        count_s1 = sum(s1[0].count(chr(char)) for s1 in s1)
        count_s2 = sum(s2[0].count(chr(char)) for s2 in s2)
        freqs.append(count_s1 - count_s2)

    if all(freq >= 0 for freq in freqs):
        print("YES")
    else:
        print("NO")

# Example usage
check_character_frequency_difference()


from collections import Counter

def check_character_frequency_difference():
    inputs = [input().replace(" ", "") for _ in range(2)]

    freq_s1 = Counter(inputs[0])
    freq_s2 = Counter(inputs[1])

    freqs = []
    
    for char in range(ord('A'), ord('z') + 1):
        char_str = chr(char)
        difference = freq_s1[char_str] - freq_s2[char_str]
        freqs.append(difference)

    if all(freq >= 0 for freq in freqs):
        print("YES")
    else:
        print("NO")

# Example usage
check_character_frequency_difference()
