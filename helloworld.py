def print_word(string, character_index=0, printed_string=''):
    for character in string:
        for letter in range(ord('a'), ord('z') + 1):
            print(printed_string + chr(letter))
            if chr(letter) == character:
                print_word(string[1:], character_index+1, printed_string + character)


if __name__ == '__main__':
    print_word("ab")