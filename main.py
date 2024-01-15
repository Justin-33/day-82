from morse_dict import morse_code_dict



def encript(text):
    morse_code = ' '
    for char in text:
        if ' ' in char:
            morse_code+=char
        elif char in morse_code_dict:
            morse_code += morse_code_dict[char]
    return morse_code
            
        
def decript(morse_code):
    morse_code = morse_code.split(' ')
    text = ' '
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text += key

    return text


english_input = input("type in a word: ").upper()
print(english_input)
morse_code = encript(english_input)
print(f"the morse code of your word is {morse_code}")



morsecode_input = input("type in a code: ")
print(morsecode_input)
decript_word = decript(morsecode_input)
print(f"the morse code of your word is {decript_word}")