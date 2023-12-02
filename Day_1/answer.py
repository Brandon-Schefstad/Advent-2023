from operator import is_
import time


def my_function_to_run(input: str):
    total = 0
    input = input.split("\n")
    for line in input:
        addend = my_helper_function(line)
        addend = int(addend)
        total += addend
    return total


def my_helper_function(input: str):
    input = list(input)
    return_int = []

    return_int.append(append(input))
    input.reverse()
    return_int.append(append(input, True))

    return "".join(return_int)


def append(input: list, is_reversed: bool = False):
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_letter = ["o", "t", "f", "s", "e", "n"]
    second_letter = ["n", "w", "h", "o", "i", "e"]

    word_dict = {
        "on": "e_1",
        "tw": "o_2",
        "th": "ree_3",
        "fo": "ur_4",
        "fi": "ve_5",
        "si": "x_6",
        "se": "ven_7",
        "ei": "ght_8",
        "ni": "ne_9",
    }
    last_letter = ["e", "o", "r", "t", "x", "n"]
    second_last_letter = ["n", "w", "e", "u", "v", "i", "h"]
    word_dict_reverse = {
        "eno": "_1",
        "owt": "_2",
        "eer": "ht_3",
        "ruo": "f_4",
        "evi": "f_5",
        "xis": "_6",
        "nev": "es_7",
        "thg": "ie_8",
        "eni": "n_9",
    }

    for index, char in enumerate(input):
        if char in integers:
            return char

        elif (
            char in first_letter
            and input[index + 1] in second_letter
            and not is_reversed
        ):
            letter_pair = f"{char}{input[index+1]}"
            if letter_pair in word_dict.keys():
                remaining_letters = word_dict[letter_pair].split("_")[0]
                value = word_dict[letter_pair].split("_")[1]
                remaining_length = len(list(remaining_letters))
                for i in range(remaining_length):
                    curr_char = input[index + i + 2]
                    if remaining_letters[i] == curr_char:
                        return value
        elif (
            char in last_letter
            and input[index + 1] in second_last_letter
            and is_reversed
        ):
            letter_triplet = f"{char}{input[index+1]}{input[index+2]}"
            if letter_triplet in word_dict_reverse.keys():
                remaining_letters = word_dict_reverse[letter_triplet].split("_")[0]
                value = word_dict_reverse[letter_triplet].split("_")[1]
                remaining_length = len(list(remaining_letters))
                if len(list(remaining_letters)):
                    for i in range(remaining_length):
                        curr_char = input[index + i + 3]
                        if remaining_letters[i] == curr_char:
                            return value
                else:
                    return value
