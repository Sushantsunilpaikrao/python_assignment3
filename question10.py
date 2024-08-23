def is_not_vowel(char):
    vowels = 'aeiouAEIOU'
    return char not in vowels

input_string = "Hello, how are you?"

result_string = ''.join(filter(is_not_vowel, input_string))

print(f"String without vowels: {result_string}")
