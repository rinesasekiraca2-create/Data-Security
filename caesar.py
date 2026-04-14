import string

# alfabeti me shkronja te vogla
ALPHABET = string.ascii_lowercase

def encrypt(text, shift):
    result = ""

    for c in text:
        # kontrollo a eshte shkronje
        if c in ALPHABET:
            # gjej poziten e shkronjes dhe shto shift
            idx = (ALPHABET.index(c) + shift) % 26
            result += ALPHABET[idx]
        else:
            # nese nuk eshte shkronje (hapesire, pike, etj)
            result += c

    return result