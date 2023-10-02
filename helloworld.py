def print_word(string, printed_string=''):
    if len(string) == 0:
        return
    if string[0] == " ":
        string = string[1:]
        printed_string += " "
    for letter in range(ord('a'), ord(string[0]) + 1):
        print(printed_string + chr(letter))
        if string[0] == chr(letter):
            print_word(string[1:], printed_string + chr(letter))


if __name__ == '__main__':
    print_word("hello world")
