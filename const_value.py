def solve(word):
    vowels = "aeiou"

    def calculate_consonant_value(substring):
        return sum(ord(character) - ord('a') + 1 for character in substring)

    max_value = 0
    constant_substrings = ""

    for character in word:
        if character not in vowels:
            constant_substrings+=character
        else:

            current_value = calculate_consonant_value(constant_substrings)
            max_value = max(max_value, current_value)
            constant_substrings = ""
    max_value = max(calculate_consonant_value(constant_substrings) , max_value)


    return max_value

if __name__ == '__main__':
    const_substring = solve("strength")
    print(const_substring)
    