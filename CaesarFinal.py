import string
from collections import Counter


ALPHABET = string.ascii_lowercase


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().lower()
    except FileNotFoundError:
        print(f"File {filename} nuk u gjet.")
        return ""

def save_output(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def calculate_frequency(text):
    filtered = [c for c in text if c in ALPHABET]
    total = len(filtered)

    freq = Counter(filtered)

    if total == 0:
        return {c: 0 for c in ALPHABET}

    return {c: freq[c] / total for c in ALPHABET}

def print_frequency(freq):
    print("\nFrekuencat e shkronjave:\n")
    for k, v in sorted(freq.items()):
        print(f"{k}: {v:.4f}")


def encrypt(text, shift):
    result = ""
    for c in text:
        if c in ALPHABET:
            idx = (ALPHABET.index(c) + shift) % 26
            result += ALPHABET[idx]
        else:
            result += c
    return result

def decrypt(text, shift):
    result = ""
    for c in text:
        if c in ALPHABET:
            idx = (ALPHABET.index(c) - shift) % 26
            result += ALPHABET[idx]
        else:
            result += c
    return result


def chi_squared(observed, expected):
    score = 0
    for c in ALPHABET:
        o = observed.get(c, 0)
        e = expected.get(c, 0)
        if e > 0:
            score += ((o - e) ** 2) / e
    return score

def break_caesar(cipher_text, reference_freq):
    best_shift = 0
    best_score = float('inf')
    best_text = ""

    print("\nDuke provuar të gjitha shift-et...\n")

    for shift in range(26):
        decrypted = decrypt(cipher_text, shift)
        freq = calculate_frequency(decrypted)
        score = chi_squared(freq, reference_freq)

        print(f"Shift {shift}: score = {score:.4f}")

        if score < best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted

    return best_shift, best_text


def main():
    print("=== Caesar Cipher Attack ===\n")

    reference = read_file("reference.txt")
    cipher = read_file("cipher.txt")

    if not reference or not cipher:
        print("Gabim: kontrollo file-at!")
        return

    ref_freq = calculate_frequency(reference)
    print_frequency(ref_freq)

    shift, decrypted = break_caesar(cipher, ref_freq)

    print("\n========================")
    print(f"Shift i gjetur: {shift}")
    print("========================\n")

    print("Teksti i dekriptuar:\n")
    print(decrypted)

    save_output("output.txt", decrypted)

    print("\nRezultati u ruajt ne output.txt")


if __name__ == "__main__":
    main()