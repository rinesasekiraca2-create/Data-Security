from caesar import decrypt
from frequency import calculate_frequency
import string

ALPHABET = string.ascii_lowercase

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

    print("\nDuke provuar 26 shift-e...\n")

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