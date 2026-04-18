# Frequency analysis functions
from collections import Counter
import string

ALPHABET = string.ascii_lowercase
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

