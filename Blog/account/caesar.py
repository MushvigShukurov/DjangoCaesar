import string


def Caesar(word,key,decrypt=False):
    result = ""
    if key == 0 :
        return word
    elif key < 0:
        key *= -1

    if decrypt:
        key *= -1

    all_sim = "yZrPIçaəŞüÜcöALTQqunjXEBƏIbohmÖDKCVisıxRvÇğYSĞUtzJgkOşGNfeMlpHdF" + string.punctuation + string.digits 
    
    for letter in word:
        letter_index = -1
        for i in all_sim:
            if letter == i:
                letter_index = all_sim.index(letter) + key
        if letter_index == -1:
            result+=letter 
            continue
        if letter_index >= len(all_sim) or letter_index < 0:
            letter_index = letter_index % len(all_sim)
        result+=all_sim[letter_index]
    return result
