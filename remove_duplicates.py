# Given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can only traverse the string at once.

def remove_duplicates(input_str):
    seen_chars = set()
    result_str = []

    for char in input_str:
        if char not in seen_chars:
            seen_chars.add(char)
            result_str.append(char)

    return ''.join(result_str)

# Example Usage:
input_string = "ababacd"
result = remove_duplicates(input_string)
print("String after removing duplicates:", result)
