def my_function_to_run(input):
    total = 0
    enumerated_games = enumerate(input.split("\n"))
    for game_index, game in enumerated_games:
        collection = game.split(";")
        collection_validity = set()
        for index, pull in enumerate(collection):
            pull_validity = parse(pull, index)
            pull_is_invalid = pull_validity[0] == False or len(list(pull_validity)) > 1
            if pull_is_invalid:
                collection_validity.add(False)
            else:
                collection_validity.add(True)
        collection_is_invalid = list(collection_validity)[0] == False or len(list(collection_validity)) > 1
        if collection_is_invalid:
            pass
        else:
            total += game_index + 1
    return total


def parse(pull, index):
    color_group = str(pull).split(",")

    if index == 0:
        color_group = pull.split(":")[1].split(",")

    color_group_is_valid = set()

    for index in range(len(color_group)):
        
        color_number_pair = color_group[index]
        [number, color] = color_number_pair.strip().split(" ")

        redcheck = int(number) > 12 and color == "red"
        greencheck = int(number) > 13 and color == "green"
        bluecheck = int(number) > 14 and color == "blue"

        if (redcheck or bluecheck or greencheck):
            color_group_is_valid.add(False)
        else:
            color_group_is_valid.add(True)
            
    return list(color_group_is_valid)
