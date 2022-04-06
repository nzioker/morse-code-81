# list of the morse code letters
morse_code = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}


# take input from user via the CLI. Should be in capital letters because the keys in the dictionary are capital
user_input = input("Enter in a Word: ").lower()


# break it up into a list of letters so that you can loop through the list
new_list = [char for char in user_input]

morse_list = []  # we'll append to this list the characters of the word the user gave that are in the morse_code list
for i in new_list:
    if morse_code[i]:
        morse_list.append(morse_code[i])

final_answer = " ".join(morse_list)  # join up the list with a space in between
print(final_answer)




