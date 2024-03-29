def read_message_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
