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

