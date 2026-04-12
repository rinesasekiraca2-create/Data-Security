def read_file(filename): # Lexon tekst nga një file dhe e kthen në lowercase

    try:

        with open(filename, 'r', encoding='utf-8') as f:

            return f.read().lower()

    except FileNotFoundError:

        print(f"File {filename} nuk u gjet.")

        return ""


def save_output(filename, text): # Ruan tekstin në një file

    with open(filename, 'w', encoding='utf-8') as f:

        f.write(text)
