

def main():
    input_text = list(open("input.txt").readline())
    alphabet_dict = {}
    for c in char_range('a', 'z'):
        alphabet_dict[c] = c.capitalize()
    for c in char_range('A', 'Z'):
        alphabet_dict[c] = c.lower()

    final_text = remove_characters(alphabet_dict, input_text)

    print(str(final_text))


def remove_characters(alphabet_dict, input_text):
    removed_text = input_text.copy()
    match_found = False
    skip = False
    for c, next_c in zip(input_text[0:], input_text[1:]):
        if not skip:
            character = alphabet_dict.get(c)
            if next_c == character:
                removed_text.remove(c)
                removed_text.remove(next_c)
                match_found = True
                skip = True
                print("removed: " + c + ", " + next_c)
        else:
            skip = False

    if match_found:
        print("next iteration")
        remove_characters(alphabet_dict, removed_text)
    else:
        return removed_text


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


if __name__ == "__main__":
    main()
