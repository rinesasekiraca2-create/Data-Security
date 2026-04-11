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
