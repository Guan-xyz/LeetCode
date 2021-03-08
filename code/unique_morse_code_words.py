# 804. Unique Morse Code Words


def unique_morese_representations(words):
    letters_to_morse = {}
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.",
                      "....","..",".---","-.-",".-..","--","-.",
                      "---",".--.","--.-",".-.","...","-","..-",
                      "...-",".--","-..-","-.--","--.."]
    for i in range(len(morse_code)):
        letters_to_morse[chr(97+i)] = morse_code[i]
    result = []
    for j in words:
        code = ''
        for k in j:
            code == letters_to_morse[k]
        if code not in result:
            result.append(code)
        code = ''
    return len(result)
