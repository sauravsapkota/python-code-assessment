def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last seen index of characters
    char_index_map = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        # If the character is already in the substring, move the start pointer
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        # Update the character's last seen index
        char_index_map[char] = end

        # Calculate the length of the current substring
        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage
s = "abcdabcbb"
print(length_of_longest_substring(s))
