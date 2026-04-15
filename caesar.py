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

# dekripton tekstin duke hequr shift (kthen tekstin origjinal)
def decrypt(text, shift):
    result = ""

    for c in text:
        if c in ALPHABET:
            # heq shift per me kthy shkronjen origjinale
            idx = (ALPHABET.index(c) - shift) % 26
            result += ALPHABET[idx]
        else:
            result += c

    return result



