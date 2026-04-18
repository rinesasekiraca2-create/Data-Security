from file_utils import read_file, save_output

from frequency import calculate_frequency, print_frequency

from attack import break_caesar

def main():

    print("=== Caesar Cipher Attack ===\n")



    reference = read_file("reference.txt")

    cipher = read_file("cipher.txt")


    if not reference or not cipher:

        print("Gabim me file-at!")

        return

    ref_freq = calculate_frequency(reference)

    print_frequency(ref_freq)

    shift, decrypted = break_caesar(cipher, ref_freq)

    print("\n========================")
    print(f"SHIFT I GJETUR: {shift}")
    print("========================\n")

    print("TEKSTI I DEKRIPTUAR:\n")
    print(decrypted)

    save_output("output.txt", decrypted)

    print("\n U ruajt ne output.txt")


if __name__ == "__main__":
    main()