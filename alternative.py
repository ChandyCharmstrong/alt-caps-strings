def alternate_string_case(input_string):
    characters = list(input_string)
    for i in range(len(characters)):
        if i % 2 == 0:
            characters[i] = characters[i].upper()
        else:
            characters[i] = characters[i].lower()
    return ''.join(characters)

def alternate_word_case(input_string):
    words = input_string.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return ' '.join(words)

input_string = input("Write a sentence: ")
result = alternate_string_case(input_string)
print("Result (alt letters):", result)

result = alternate_word_case(input_string)
print("Result (alt words):", result)
